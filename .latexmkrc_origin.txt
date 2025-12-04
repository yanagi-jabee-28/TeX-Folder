#!/usr/bin/env perl
# ローカルな latexmk 設定ファイル (.latexmkrc)
# Windows でも問題なく動作するように、各実行コマンドを定義しています。

# 通常の LaTeX ドキュメント用のコマンド
$latex = 'uplatex %O -kanji=utf8 -no-guess-input-enc -synctex=1 -interaction=nonstopmode %S'; 
# pdfLaTeX 用のコマンド 
$pdflatex = 'pdflatex %O -synctex=1 -interaction=nonstopmode %S'; 
# LuaLaTeX 用のコマンド 
$lualatex = 'lualatex %O -synctex=1 -interaction=nonstopmode %S'; 
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

# $pdf_mode ...PDF の作成方法を指定するオプション 
# 0: $latex で .tex -> .dvi するだけ
# 1: $pdflatex で .tex -> .pdf (pdflatexは英文にしか使えない)
# 2: $latex で .tex -> .dvi / $dvips で .dvi -> .ps / $ps2pdf で .ps -> PDF
# 3: $latex で .tex -> .dvi / $dvipdf で .dvi -> PDF 
# 4: $lualatex で .tex -> PDF
# 5: $xelatex で .tex -> .xdv / $xdvipdfmx で .xdv -> PDF

# 何も設定しなければ、latexmk の呼び出し引数に応じて自動判定されるため
# 必要に応じて 4 をデフォルト化可能です。luaonly 環境なら下行のコメントを外す。
# $pdf_mode = 4; 

# PDFビューワ の設定 
$pdf_previewer = ""; # コンパイル成功時に自動で外部ビューアを開かせない

# 一時ファイルの自動削除設定
$clean_ext = "aux bbl blg fls fdb_latexmk figlist makefile synctex.gz run.xml";

# ビルド後に自動クリーンアップを実行
$cleanup_mode = 1;

# 追加で削除したいファイルの拡張子
push @generated_exts, "figlist", "makefile", "run.xml";

# latexmkの管理ファイルも削除したい場合（通常は推奨しない）
# $clean_full_mode = 1;  # コメントアウト推奨
