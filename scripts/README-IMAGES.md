画像最適化スクリプト

目的
- 高解像度画像によるLaTeXコンパイル遅延を減らすため，画像をダウンサンプリングして`image/optimized/`に保存します。

使い方（PowerShell, Windows）
1. ImageMagick をインストールし，`magick` が PATH にあることを確認してください。
2. スクリプトを実行します（リポジトリルートから）。`-TargetDir` で任意の画像フォルダを指定できます:

```powershell
# default: 対象フォルダを自動検出
cd scripts
./optimize-images.ps1 -MaxSize 1600 -Quality 85

# 明示的に画像フォルダを指定する例
./optimize-images.ps1 -TargetDir "..\Experiment\9_高周波線路\image" -MaxSize 1600 -Quality 85
```

- `-MaxSize` は長辺の最大ピクセル数（デフォルト 1600）。
- `-Quality` は JPEG 圧縮品質（デフォルト 85）。
- `-Force` を付けると既存の最適化画像を上書きします。

TeX 側の設定
- `9_High.tex` は `image/optimized/` を優先して画像を読み込みます。`image/optimized/` に最適化画像があればそれを使用し，なければ元の `image/` の画像を使用します。

備考
- SVG の扱いはリポジトリごとに異なります（必要なら別途ラスタライズ処理を追加してください）。
- スクリプトは PNG/JPG/TIFF に対応しています。