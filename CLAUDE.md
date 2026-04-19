# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 概要

統合版マイクラ(Bedrock Edition)のスーパーフラットワールドをカスタマイズするツール。  
`level.dat`のバイナリを直接編集し、地形レイヤー・バイオーム・シード値・ワールド名を変更した`.mcworld`ファイルを生成する。

## 実行方法

```bash
python main.py
```

`config.py`を編集してから実行する。出力は`{WORLD_NAME}.mcworld`。

## アーキテクチャ

`config.py` → `main.py` の2ファイル構成。

**`config.py`**: ユーザーが編集する設定ファイル。`WORLD_NAME`, `SEED`, `BIOME_ID`, `BLOCK_LAYERS`, `WORLD_ICON_PATH`, `LEVEL_DAT` を定義。

**`main.py`** の処理フロー:
1. `read_level_dat()` — `level.dat`をバイナリ読み込み
2. `split_binary()` — `FlatWorldLayers`, `LevelName`, `RandomSeed` の3タグを境にバイナリを4セグメントに分割（テンプレートとして保持）
3. `build_flat_world_layers()` / `build_level_name()` / `build_random_seed()` — 各フィールドの新バイナリを生成
4. `build_level_dat()` — テンプレートセグメントと新データを結合。先頭8バイトのファイルサイズフィールドも更新
5. `create_mcworld()` — `level.dat`と`world_icon.jpeg`をZIP圧縮して`.mcworld`を出力

## バイナリ構造の注意点

- `FlatWorldLayers`の値はJSON文字列＋`\x00`終端のUTF-8バイト列、先頭2バイト(little-endian)が長さ
- `LevelName`も同じTAG_String形式（2バイト長＋UTF-8）
- `RandomSeed`はTAG_Long（8バイト、little-endian符号付き整数）
- `level.dat`の先頭8バイトはヘッダー（バージョン4バイト＋ファイルサイズ4バイト）、`build_level_dat()`でサイズを再計算する

## コーディングルール

- 型ヒントを付ける
- docstringは日本語で書く

## `.trash/original-files` について

mcworldのファイル構造参照用。バイナリファイルが多いため直接Readしないこと。
