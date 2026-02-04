変更点と出力ファイル

- 作成ファイル:
  - `pattern_data_clean.csv` — 数値のみの入力データ（元CSVに式が入っていたためクリーンコピー）
  - `相関解析課題_kaito.xlsx` — ラベル、検算用のExcel式、散布図（回帰直線・R^2表示）、結果ブロックを含む提出用ファイル
  - `scatter_correlation.png` — 提出用の高解像度散布図（回帰直線と注記付き）
  - `generate_correlation_xlsx.py` — 再現用スクリプト（実行すると上記を生成）

- 使い方
  1. 必要パッケージをインストール: `pip install pandas numpy matplotlib scipy xlsxwriter`
  2. スクリプト実行: `python generate_correlation_xlsx.py`

- 推奨: `相関解析課題_kaito.xlsx` を開いて式とグラフを確認し、氏名をファイル名に付けて提出してください。
