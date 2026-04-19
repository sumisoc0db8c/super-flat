"""スーパーフラットワールドの設定定義"""

# --- ワールド基本設定 ---
WORLD_NAME: str = "sumiso creative テンプレート"
SEED: int = 141

# --- 地形レイヤー設定 ---
# 下から順に積み上げる
BLOCK_LAYERS: list[dict[str, str | int]] = [
    {"block_name": "minecraft:bedrock", "count": 1},
    {"block_name": "minecraft:gray_concrete", "count": 63},
    {"block_name": "minecraft:gray_concrete", "count": 100},
]

# --- バイオーム設定 ---
# バイオームID一覧 (Bedrock Edition)
# https://minecraft.wiki/w/Biome/ID
BIOME_IDS: dict[str, int] = {
    # --- オーバーワールド ---
    "ocean": 0,
    "plains": 1,
    "desert": 2,
    "windswept_hills": 3,
    "forest": 4,
    "taiga": 5,
    "swamp": 6,
    "river": 7,
    "legacy_frozen_ocean": 10,
    "frozen_river": 11,
    "snowy_plains": 12,
    "snowy_mountains": 13,
    "mushroom_fields": 14,
    "mushroom_island_shore": 15,
    "beach": 16,
    "desert_hills": 17,
    "wooded_hills": 18,
    "taiga_hills": 19,
    "mountain_edge": 20,
    "jungle": 21,
    "jungle_hills": 22,
    "sparse_jungle": 23,
    "deep_ocean": 24,
    "stony_shore": 25,
    "snowy_beach": 26,
    "birch_forest": 27,
    "birch_forest_hills": 28,
    "dark_forest": 29,
    "snowy_taiga": 30,
    "snowy_taiga_hills": 31,
    "old_growth_pine_taiga": 32,
    "giant_tree_taiga_hills": 33,
    "windswept_forest": 34,
    "savanna": 35,
    "savanna_plateau": 36,
    "badlands": 37,
    "wooded_badlands": 38,
    "badlands_plateau": 39,
    "warm_ocean": 40,
    "deep_warm_ocean": 41,
    "lukewarm_ocean": 42,
    "deep_lukewarm_ocean": 43,
    "cold_ocean": 44,
    "deep_cold_ocean": 45,
    "frozen_ocean": 46,
    "deep_frozen_ocean": 47,
    "bamboo_jungle": 48,
    "bamboo_jungle_hills": 49,
    "sunflower_plains": 129,
    "desert_lakes": 130,
    "windswept_gravelly_hills": 131,
    "flower_forest": 132,
    "taiga_mountains": 133,
    "swamp_hills": 134,
    "ice_spikes": 140,
    "modified_jungle": 149,
    "modified_jungle_edge": 151,
    "old_growth_birch_forest": 155,
    "tall_birch_hills": 156,
    "dark_forest_hills": 157,
    "snowy_taiga_mountains": 158,
    "old_growth_spruce_taiga": 160,
    "giant_spruce_taiga_hills": 161,
    "gravelly_mountains_plus": 162,
    "windswept_savanna": 163,
    "shattered_savanna_plateau": 164,
    "eroded_badlands": 165,
    "modified_wooded_badlands_plateau": 166,
    "modified_badlands_plateau": 167,
    # --- ネザー ---
    "nether_wastes": 8,
    "soul_sand_valley": 178,
    "crimson_forest": 179,
    "warped_forest": 180,
    "basalt_deltas": 181,
    # --- ジ・エンド ---
    "the_end": 9,
    # --- 1.18以降 ---
    "jagged_peaks": 182,
    "frozen_peaks": 183,
    "snowy_slopes": 184,
    "grove": 185,
    "meadow": 186,
    "lush_caves": 187,
    "dripstone_caves": 188,
    "stony_peaks": 189,
    "deep_dark": 190,
    "mangrove_swamp": 191,
    "cherry_grove": 192,
    "pale_garden": 193,
}

BIOME_ID: int = BIOME_IDS["taiga"]

# --- ファイルパス設定 ---
WORLD_ICON_PATH: str = "world_icon.jpeg"
LEVEL_DAT:str = "level.dat"
