#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF を Markdown 形式に変換する統合スクリプト
最適化されたテキスト抽出とレイアウト修正を実装
"""

import sys
from pathlib import Path
import re
import argparse

try:
    import pdfplumber
except ImportError:
    print("pdfplumber がインストールされていません。インストール中...")
    import subprocess
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "pdfplumber"])
    import pdfplumber


def is_empty_table(table):
    """テーブルが空またはレイアウト用かどうかを判定"""
    if not table or len(table) < 2:
        return True

    all_empty = all(
        cell is None or (isinstance(cell, str) and cell.strip() == '')
        for row in table
        for cell in row
    )
    if all_empty:
        return True

    empty_count = sum(
        1 for row in table
        for cell in row
        if cell is None or (isinstance(cell, str) and cell.strip() == '')
    )
    total_cells = len(table) * len(table[0]) if table else 1

    return empty_count / total_cells > 0.7


def is_heading(line):
    """行が見出しであるかを判定"""
    line = line.strip()

    if not line:
        return False

    # セクション番号パターン（「1」「2 見出し」など）
    if re.match(r'^(\d+)\s*(.*)$', line) and len(line) < 50:
        return True

    # 特定のキーワード
    heading_keywords = ['概要', '研究', '手法', '結果',
                        '結論', '参考文献', '謝辞', 'はじめに', 'まとめ']
    if any(kw in line for kw in heading_keywords):
        return True

    return False


def clean_and_restructure_text(text):
    """テキストをクリーンアップし、段落を適切に再構成"""
    if not text:
        return ""

    # 複数の空行を1つに統一
    text = re.sub(r'\n\n+', '\n\n', text)

    lines = text.split('\n')
    restructured_lines = []
    current_paragraph = []

    for line in lines:
        # 行のクリーンアップ
        line = line.strip()

        if not line:
            # 空行: 現在の段落を出力
            if current_paragraph:
                para_text = ' '.join(current_paragraph)
                # 分割された日本語を結合
                para_text = re.sub(
                    r'([ぁ-ん一-龯])\s+([ぁ-ん一-龯])', r'\1\2', para_text)
                para_text = re.sub(
                    r'([ぁ-ん一-龯])\s+([a-zA-Z])', r'\1\2', para_text)
                para_text = re.sub(
                    r'([a-zA-Z])\s+([ぁ-ん一-龯])', r'\1\2', para_text)
                restructured_lines.append(para_text)
                current_paragraph = []
            restructured_lines.append('')  # 空行を保持
        elif is_heading(line):
            # 見出し行
            if current_paragraph:
                para_text = ' '.join(current_paragraph)
                para_text = re.sub(
                    r'([ぁ-ん一-龯])\s+([ぁ-ん一-龯])', r'\1\2', para_text)
                restructured_lines.append(para_text)
                current_paragraph = []
            restructured_lines.append('')
            restructured_lines.append(f"### {line}")
            restructured_lines.append('')
        else:
            # 通常のテキスト行
            current_paragraph.append(line)

    # 最後の段落を処理
    if current_paragraph:
        para_text = ' '.join(current_paragraph)
        para_text = re.sub(r'([ぁ-ん一-龯])\s+([ぁ-ん一-龯])', r'\1\2', para_text)
        restructured_lines.append(para_text)

    result = '\n'.join(restructured_lines).strip()
    # 複数の連続した空行を削除
    result = re.sub(r'\n\n\n+', '\n\n', result)

    return result


def extract_pdf_to_markdown(pdf_path, output_path=None):
    """
    PDFからMarkdownへの変換（最適化版）

    Args:
        pdf_path: PDFファイルのパス
        output_path: 出力するMarkdownファイルのパス
    """
    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        print(f"エラー: ファイルが見つかりません: {pdf_path}")
        return False

    # 出力パスの設定
    if output_path is None:
        output_path = pdf_path.with_stem(
            pdf_path.stem + '_extracted').with_suffix('.md')
    else:
        output_path = Path(output_path)

    print(f"PDFファイルを読み込んでいます: {pdf_path}")

    try:
        with pdfplumber.open(pdf_path) as pdf:
            total_pages = len(pdf.pages)
            print(f"総ページ数: {total_pages}\n")

            markdown_content = []
            markdown_content.append(f"# {pdf_path.stem}\n\n")
            markdown_content.append(f"**出典**: {pdf_path.name}  \n")
            markdown_content.append(f"**総ページ数**: {total_pages}  \n")
            markdown_content.append(
                f"**抽出日時**: {__import__('datetime').datetime.now().strftime('%Y年%m月%d日')}\n\n")
            markdown_content.append("---\n\n")

            # 各ページのテキストを抽出
            for page_num, page in enumerate(pdf.pages, 1):
                print(f"ページ {page_num}/{total_pages} を処理中...")

                # ページヘッダー
                markdown_content.append(f"## ページ {page_num}\n\n")

                # テキスト抽出（最適化版）
                text = page.extract_text()
                if text:
                    cleaned_text = clean_and_restructure_text(text)
                    if cleaned_text:
                        markdown_content.append(cleaned_text)
                        markdown_content.append("\n\n")

                # テーブル抽出（有効なテーブルのみ）
                tables = page.extract_tables()
                if tables:
                    valid_tables = [t for t in tables if not is_empty_table(t)]

                    if valid_tables:
                        markdown_content.append("#### 表\n\n")
                        for table_num, table in enumerate(valid_tables, 1):
                            table_md = _convert_table_to_markdown(table)
                            if table_md.strip():
                                markdown_content.append(table_md)
                                markdown_content.append("\n\n")

                markdown_content.append("---\n\n")

            # Markdownファイルに出力
            output_text = ''.join(markdown_content)

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(output_text)

            print(f"\n✓ 完了! Markdown ファイルに出力されました: {output_path}")
            print(f"  ファイルサイズ: {output_path.stat().st_size} バイト")
            print(f"\n💡 ヒント: 自動抽出結果を基に手動で整形することを推奨します。")

            return True

    except Exception as e:
        print(f"エラーが発生しました: {e}")
        import traceback
        traceback.print_exc()
        return False


def _convert_table_to_markdown(table):
    """テーブルデータを Markdown テーブル形式に変換"""
    if not table or len(table) == 0:
        return ""

    # ヘッダー行を取得
    header = table[0]
    markdown_lines = []

    # ヘッダー
    markdown_lines.append(
        "| " + " | ".join(str(cell).strip() if cell else "" for cell in header) + " |")

    # セパレータ
    markdown_lines.append("| " + " | ".join(["---"] * len(header)) + " |")

    # データ行
    for row in table[1:]:
        markdown_lines.append(
            "| " + " | ".join(str(cell).strip() if cell else "" for cell in row) + " |")

    return "\n".join(markdown_lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='PDFをMarkdown形式に変換')
    parser.add_argument('pdf_file', nargs='?', help='変換するPDFファイルのパス')
    parser.add_argument('-o', '--output', help='出力するMarkdownファイルのパス')

    args = parser.parse_args()

    # デフォルトのPDFファイルパス
    if args.pdf_file:
        pdf_file = Path(args.pdf_file)
    else:
        # スクリプトからの相対パスで18_167.pdfを指定
        pdf_file = Path(__file__).parent.parent / "資料" / "18_167.pdf"

    # 出力パス
    output_file = Path(args.output) if args.output else None

    success = extract_pdf_to_markdown(pdf_file, output_file)
    sys.exit(0 if success else 1)
