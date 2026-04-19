"""統合版マイクラ カスタムスーパーフラット生成ツール"""

import json
import struct
import zipfile

import config


def read_level_dat(filepath: str) -> bytes:
    """level.datファイルをバイナリとして読み込む"""
    with open(filepath, "rb") as f:
        return f.read()


def find_tag(data: bytes, tag_name: str) -> int:
    """NBTタグ名のバイト位置を検索する"""
    pos = data.find(tag_name.encode("utf-8"))
    if pos == -1:
        raise ValueError(f"NBTタグが見つかりません: {tag_name}")
    return pos


def split_binary(data: bytes) -> tuple[bytes, bytes, bytes, bytes]:
    """level.datバイナリをテンプレート部分に分割する

    FlatWorldLayers, LevelName, RandomSeedの3タグの位置を特定し、
    編集可能なデータ部分を除いた4つのテンプレートセグメントを返す。
    """
    # FlatWorldLayers (TAG_String): タグ名 + 2バイト長 + ペイロード
    fwl_pos = find_tag(data, "FlatWorldLayers")
    fwl_name_end = fwl_pos + len(b"FlatWorldLayers")
    fwl_payload_len = struct.unpack("<H", data[fwl_name_end : fwl_name_end + 2])[0]
    fwl_data_end = fwl_name_end + 2 + fwl_payload_len

    # LevelName (TAG_String): タグ名 + 2バイト長 + ペイロード
    ln_pos = find_tag(data, "LevelName")
    ln_name_end = ln_pos + len(b"LevelName")
    ln_payload_len = struct.unpack("<H", data[ln_name_end : ln_name_end + 2])[0]
    ln_data_end = ln_name_end + 2 + ln_payload_len

    # RandomSeed (TAG_Long): タグ名 + 8バイト固定
    rs_pos = find_tag(data, "RandomSeed")
    rs_name_end = rs_pos + len(b"RandomSeed")
    rs_data_end = rs_name_end + 8

    head = data[:fwl_name_end]
    after_fwl = data[fwl_data_end:ln_name_end]
    after_level_name = data[ln_data_end:rs_name_end]
    after_seed = data[rs_data_end:]

    return head, after_fwl, after_level_name, after_seed


def build_flat_world_layers(
    biome_id: int, block_layers: list[dict[str, str | int]]
) -> bytes:
    """FlatWorldLayersのバイナリデータを生成する"""
    flat_json = {
        "biome_id": biome_id,
        "block_layers": block_layers,
        "encoding_version": 6,
        "preset_id": None,
        "world_version": "version.post_1_18",
    }
    json_bytes = json.dumps(flat_json, separators=(",", ":")).encode("utf-8")
    payload = json_bytes + b"\x00"
    length = struct.pack("<H", len(payload))
    return length + payload


def build_level_name(world_name: str) -> bytes:
    """LevelNameのバイナリデータを生成する"""
    name_bytes = world_name.encode("utf-8")
    length = struct.pack("<H", len(name_bytes))
    return length + name_bytes


def build_random_seed(seed: int) -> bytes:
    """RandomSeedのバイナリデータを生成する"""
    return struct.pack("<q", seed)


def build_level_dat(
    head: bytes,
    after_fwl: bytes,
    after_level_name: bytes,
    after_seed: bytes,
    fwl_data: bytes,
    level_name_data: bytes,
    seed_data: bytes,
) -> bytes:
    """テンプレート部分と新しいデータを結合してlevel.datバイナリを構築する"""
    binary = (
        head
        + fwl_data
        + after_fwl
        + level_name_data
        + after_level_name
        + seed_data
        + after_seed
    )
    file_size = len(binary) - 8
    binary = binary[:4] + struct.pack("<I", file_size) + binary[8:]
    return binary


def create_mcworld(level_dat: bytes, world_name: str, icon_path: str) -> str:
    """mcworldファイルを生成する"""
    output_path = f"{world_name}.mcworld"
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.writestr("level.dat", level_dat)
        zipf.write(icon_path, "world_icon.jpeg")
    return output_path


if __name__ == "__main__":
    # level.dat読み込み
    data = read_level_dat(config.LEVEL_DAT)

    # テンプレート分割
    head, after_fwl, after_level_name, after_seed = split_binary(data)

    # 各フィールドのバイナリ生成
    fwl_data = build_flat_world_layers(config.BIOME_ID, config.BLOCK_LAYERS)
    level_name_data = build_level_name(config.WORLD_NAME)
    seed_data = build_random_seed(config.SEED)

    # level.dat構築
    level_dat = build_level_dat(
        head, after_fwl, after_level_name, after_seed,
        fwl_data, level_name_data, seed_data,
    )

    # mcworld生成
    output = create_mcworld(level_dat, config.WORLD_NAME, config.WORLD_ICON_PATH)
    print(f"生成完了: {output}")
