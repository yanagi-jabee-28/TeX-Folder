<#
.SYNOPSIS
    Wordファイル(.docx/.doc)をテキストファイルに変換するスクリプト

.DESCRIPTION
    Microsoft Word COMオブジェクトを使用してWordファイルの内容を抽出し、
    テキストファイル(.txt)として保存します。

.PARAMETER WordFile
    変換するWordファイルのパス（必須）

.PARAMETER OutputFile
    出力先のテキストファイルパス（省略時は元ファイル名.txt）

.EXAMPLE
    .\ConvertWordToText.ps1 -WordFile "document.docx"
    
.EXAMPLE
    .\ConvertWordToText.ps1 -WordFile "document.docx" -OutputFile "output.txt"
#>

param(
	[Parameter(Mandatory = $true, Position = 0)]
	[string]$WordFile,
    
	[Parameter(Mandatory = $false, Position = 1)]
	[string]$OutputFile = ""
)

# エラーハンドリング
$ErrorActionPreference = "Stop"

try {
	# Wordファイルの存在確認
	if (-not (Test-Path $WordFile)) {
		throw "指定されたファイルが見つかりません: $WordFile"
	}

	# 絶対パスに変換
	$WordFile = (Resolve-Path $WordFile).Path

	# 出力ファイル名の設定
	if ([string]::IsNullOrEmpty($OutputFile)) {
		$OutputFile = [System.IO.Path]::ChangeExtension($WordFile, ".txt")
	}

	Write-Host "変換を開始します..." -ForegroundColor Cyan
	Write-Host "入力: $WordFile"
	Write-Host "出力: $OutputFile"

	# Word COMオブジェクトを作成
	Write-Host "`nWordアプリケーションを起動中..." -ForegroundColor Yellow
	$Word = New-Object -ComObject Word.Application
	$Word.Visible = $false

	# Wordファイルを開く
	Write-Host "ファイルを読み込み中..." -ForegroundColor Yellow
	$Doc = $Word.Documents.Open($WordFile, $false, $true) # ReadOnly = true

	# テキストを抽出
	Write-Host "テキストを抽出中..." -ForegroundColor Yellow
	$Text = $Doc.Content.Text

	# ファイルを閉じる
	$Doc.Close($false)
	$Word.Quit()

	# COMオブジェクトを解放
	[System.Runtime.Interopservices.Marshal]::ReleaseComObject($Doc) | Out-Null
	[System.Runtime.Interopservices.Marshal]::ReleaseComObject($Word) | Out-Null
	[System.GC]::Collect()
	[System.GC]::WaitForPendingFinalizers()

	# テキストファイルに保存（UTF-8 BOM付き）
	Write-Host "テキストファイルに保存中..." -ForegroundColor Yellow
	$Text | Out-File -FilePath $OutputFile -Encoding UTF8

	Write-Host "`n✓ 変換が完了しました！" -ForegroundColor Green
	Write-Host "出力ファイル: $OutputFile" -ForegroundColor Green
    
	# 統計情報を表示
	$lines = ($Text -split "`n").Count
	$chars = $Text.Length
	Write-Host "`n統計情報:" -ForegroundColor Cyan
	Write-Host "  行数: $lines"
	Write-Host "  文字数: $chars"

}
catch {
	Write-Host "`n✗ エラーが発生しました: $($_.Exception.Message)" -ForegroundColor Red
    
	# Wordプロセスのクリーンアップ
	if ($Word) {
		try {
			$Word.Quit()
			[System.Runtime.Interopservices.Marshal]::ReleaseComObject($Word) | Out-Null
		}
		catch {}
	}
    
	exit 1
}
finally {
	# 最終クリーンアップ
	[System.GC]::Collect()
	[System.GC]::WaitForPendingFinalizers()
}
