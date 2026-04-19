![world_icon](world_icon.jpeg)

# 統合版マイクラ カスタムスーパーフラット生成ツール

統合版マイクラ(Bedrock Edition)のスーパーフラットワールドをカスタマイズするツールです。  
`level.dat`のバイナリを編集し、地形レイヤー・バイオーム・シード値・ワールド名を変更した`.mcworld`ファイルを生成します。

## 必要なもの

- Python 3.10以上
- 標準ライブラリのみ使用(外部パッケージ不要)

## ダウンロード

本リポジトリで作成した`.mcworld`ファイルは[Releases](https://github.com/sumisoc0db8c/super-flat/releases)からダウンロードできます。  
ダウンロードしたファイルをダブルクリックするとマイクラにインポートされます。

## 使い方（カスタマイズする場合）

### 1. `config.py`を編集する

```python
WORLD_NAME = "my world"        # ワールド名
SEED = 141                     # シード値
BIOME_ID = BIOME_IDS["taiga"]  # バイオーム（BIOME_IDSから選択）

# 地形レイヤー（下から順に積み上げ）
BLOCK_LAYERS = [
    {"block_name": "minecraft:bedrock", "count": 1},
    {"block_name": "minecraft:gray_concrete", "count": 63},
    {"block_name": "minecraft:gray_concrete", "count": 100},
]

# ワールドアイコン画像（800x450）
WORLD_ICON_PATH = "world_icon.jpeg"
```

### 2. スーパーフラット生成

```bash
python main.py
```

`{ワールド名}.mcworld`ファイルが生成されます。

### 3. マイクラにインポートする

生成された`.mcworld`ファイルをダブルクリックするとマイクラが起動し、ワールドがインポートされます。

## 設定項目

| 項目 | 説明 |
|---|---|
| `WORLD_NAME` | ワールド名（日本語対応） |
| `SEED` | シード値（整数） |
| `BIOME_ID` | バイオームID（`BIOME_IDS`辞書から選択） |
| `BLOCK_LAYERS` | 地形レイヤー定義（下から順） |
| `WORLD_ICON_PATH` | ワールドアイコンのjpeg画像パス |

バイナリファイルの構造解説  
https://qiita.com/sumiso_c0db8c/items/faeb6dd2591975a89047  

## バイオームID一覧

`config.py`の`BIOME_IDS`辞書に全バイオームが定義されています。よく使うものを抜粋:

| 名前 | ID | 説明 |
|---|---|---|
| plains | 1 | 平原 |
| desert | 2 | 砂漠 |
| forest | 4 | 森林 |
| taiga | 5 | タイガ |
| swamp | 6 | 沼地 |
| snowy_plains | 12 | 雪原 |
| jungle | 21 | ジャングル |
| savanna | 35 | サバンナ |
| badlands | 37 | 荒野 |
| deep_dark | 190 | ディープダーク |

正確な全バイオームIDは[Minecraft Wiki](https://minecraft.wiki/w/Biome/ID)を参照してください。

## ブロックレイヤーの設定例

### デフォルト（クラシックフラット）
```python
BLOCK_LAYERS = [
    {"block_name": "minecraft:bedrock", "count": 1},
    {"block_name": "minecraft:dirt", "count": 2},
    {"block_name": "minecraft:grass_block", "count": 1},
]
```

### コンクリート高さ100
```python
BLOCK_LAYERS = [
    {"block_name": "minecraft:bedrock", "count": 1},
    {"block_name": "minecraft:gray_concrete", "count": 63},
    {"block_name": "minecraft:gray_concrete", "count": 100},
]
```

## 注意事項

- `block_name`はマイクラのコマンドで使うブロック名と同じ形式です（`minecraft:`プレフィックス付き）
- 最終動作確認バージョン: 統合版マイクラ v26.13
