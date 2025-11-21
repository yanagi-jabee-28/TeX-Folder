#!/usr/bin/env perl

#================================================================
# コマンド定義
#================================================================
# 通常の LaTeX ドキュメント用のコマンド (upLaTeX)
$latex = 'uplatex %O -kanji=utf8 -no-guess-input-enc -synctex=1 -interaction=nonstopmode %S';
# pdfLaTeX 用のコマンド
$pdflatex = 'pdflatex %O -synctex=1 -interaction=nonstopmode %S';

# ▼▼▼【変更点1】▼▼▼
# -shell-escape オプションを追加しました
$lualatex = 'lualatex %O -synctex=1 -interaction=nonstopmode -shell-escape %S';

# XeLaTeX 用のコマンド
$xelatex = 'xelatex %O -no-pdf -synctex=1 -shell-escape -interaction=nonstopmode %S';
# Biber, BibTeX 用のコマンド
$biber = 'biber %O --bblencoding=utf8 -u -U --output_safechars %B';
$bibtex = 'upbibtex %O %B';
# makeindex 用のコマンド
$makeindex = 'upmendex %O -o %D %S';
# dvipdf のコマンド
$dvipdf = 'dvipdfmx %O -o %D %S';
# dvips のコマンド
$dvips = 'dvips %O -z -f %S | convbkmk -u > %D';
$ps2pdf = 'ps2pdf.exe %O %S %D';

#================================================================
# PDF生成モード
#================================================================
# $pdf_mode ...PDF の作成方法を指定するオプション
# 0: .dvi まで (PDFを作成しない)
# 1: pdflatex で .tex -> .pdf
# 2: latex -> dvips -> ps2pdf
# 3: latex -> dvipdfmx
# 4: lualatex で .tex -> .pdf
# 5: xelatex で .tex -> .xdv -> xdvipdfmx
#
# ▼▼▼【変更点2】▼▼▼
# LuaLaTeX をデフォルトにするため 4 に変更しました
$pdf_mode = 4;

#================================================================
# PDFビューワ
#================================================================
$pdf_previewer = "";

#================================================================
# クリーンアップ設定
#================================================================
$clean_ext = 'aux bbl blg idx ind lof lot out toc acn acr alg glg glo gls ist fls log fdb_latexmk synctex.gz nav snm vrb figlist makefile run.xml bcf ilg nlo nls auxlock';

# _minted ディレクトリなど、特定のパターンを持つファイル/ディレクトリも削除対象に追加
push @generated_exts, '_minted*';
push @generated_exts, '*.svg'; 
# ↑ svgパッケージが生成する中間ファイルも消したい場合は追加しても良いですが、
#   再ビルド時間が伸びるので、必須ではありません。

# ビルド後に自動クリーンアップを実行
# 0: しない, 1: 成功時のみ, 2: 常に実行
$cleanup_mode = 1;