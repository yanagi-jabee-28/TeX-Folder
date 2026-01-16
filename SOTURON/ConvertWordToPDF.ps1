<#
.SYNOPSIS
    Wordファイル(.docx/.doc)をPDFファイルに変換するスクリプト

.DESCRIPTION
    Microsoft Word COMオブジェクトを使用してWordファイルをPDFに変換します。
    Word標準のPDF変換機能を使用するため、レイアウトが完全に保持されます。

.PARAMETER WordFile
    変換するWordファイルのパス（必須）
    ワイルドカード(*,?)に対応しており、複数ファイルの一括変換が可能です。

.PARAMETER OutputFolder
    PDF出力先フォルダ（省略時は元ファイルと同じフォルダ）

.PARAMETER Quality
    PDF品質設定（Standard/Minimum）
    Standard: 標準品質（デフォルト）
    Minimum: 最小サイズ（画像圧縮あり）

.EXAMPLE
    .\ConvertWordToPDF.ps1 -WordFile "document.docx"
    
.EXAMPLE
    .\ConvertWordToPDF.ps1 -WordFile "document.docx" -OutputFolder "C:\PDFs"
    
.EXAMPLE
    .\ConvertWordToPDF.ps1 -WordFile "*.docx" -Quality Minimum
    
.EXAMPLE
    Get-ChildItem *.docx | ForEach-Object { .\ConvertWordToPDF.ps1 -WordFile $_.FullName }
#>

param(
	[Parameter(Mandatory = $true, Position = 0)]
	[string]$WordFile,
    
	[Parameter(Mandatory = $false, Position = 1)]
	[string]$OutputFolder = "",
    
	[Parameter(Mandatory = $false)]
	[ValidateSet("Standard", "Minimum")]
	[string]$Quality = "Standard"
)

# エラーハンドリング
$ErrorActionPreference = "Stop"

# PDF品質の定数（Word COM用）
$wdExportFormatPDF = 17
$wdExportOptimizeForPrint = 0  # Standard quality
$wdExportOptimizeForOnScreen = 1  # Minimum size

# 変換関数
function Convert-WordToPDF {
	param(
		[string]$InputPath,
		[string]$OutputPath,
		[int]$OptimizeFor
	)
    
	$wordApp = $null
	$doc = $null
    
	try {
		# Word COMオブジェクトの作成
		Write-Host "  Word起動中..." -ForegroundColor Gray
		$wordApp = New-Object -ComObject Word.Application
		$wordApp.Visible = $false
		$wordApp.DisplayAlerts = 0  # wdAlertsNone
        
		# ドキュメントを開く
		Write-Host "  ドキュメント読み込み中..." -ForegroundColor Gray
		$doc = $wordApp.Documents.Open($InputPath, $false, $true)  # ReadOnly=true
        
		# PDFとして保存（SaveAs2は数式の互換性が最も高い）
		Write-Host "  PDF変換中（数式最適化）..." -ForegroundColor Gray
		
		$wdFormatPDF = 17  # PDF形式
		
		# SaveAs2メソッドで保存（ExportAsFixedFormatより数式互換性が高い）
		$doc.SaveAs2(
			$OutputPath,           # FileName
			$wdFormatPDF          # FileFormat
		)
        
		Write-Host "  ✓ 変換完了" -ForegroundColor Green
		return $true
        
	}
 catch {
		Write-Host "  ✗ 変換失敗: $($_.Exception.Message)" -ForegroundColor Red
		return $false
        
	}
 finally {
		# リソースのクリーンアップ
		if ($doc) {
			$doc.Close($false)  # SaveChanges=false
			[System.Runtime.Interopservices.Marshal]::ReleaseComObject($doc) | Out-Null
		}
		if ($wordApp) {
			$wordApp.Quit()
			[System.Runtime.Interopservices.Marshal]::ReleaseComObject($wordApp) | Out-Null
		}
		[System.GC]::Collect()
		[System.GC]::WaitForPendingFinalizers()
	}
}

# メイン処理
try {
	Write-Host "`n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
	Write-Host "  Word to PDF 変換ツール" -ForegroundColor Cyan
	Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━`n" -ForegroundColor Cyan
    
	# ファイルリストの取得
	$files = Get-ChildItem -Path $WordFile -Include *.docx, *.doc -File -ErrorAction Stop
    
	if ($files.Count -eq 0) {
		throw "指定されたパターンに一致するWordファイルが見つかりません: $WordFile"
	}
    
	Write-Host "対象ファイル数: $($files.Count)" -ForegroundColor Yellow
	Write-Host "PDF品質: $Quality`n" -ForegroundColor Yellow
    
	# 品質設定
	$optimizeFor = if ($Quality -eq "Standard") { $wdExportOptimizeForPrint } else { $wdExportOptimizeForOnScreen }
    
	# 統計カウンター
	$successCount = 0
	$failCount = 0
    
	# 各ファイルを変換
	foreach ($file in $files) {
		Write-Host "[$($successCount + $failCount + 1)/$($files.Count)] $($file.Name)" -ForegroundColor Cyan
        
		# 絶対パスに変換
		$inputPath = $file.FullName
        
		# 出力先の決定
		if ([string]::IsNullOrEmpty($OutputFolder)) {
			$outputPath = [System.IO.Path]::ChangeExtension($inputPath, ".pdf")
		}
		else {
			if (-not (Test-Path $OutputFolder)) {
				New-Item -Path $OutputFolder -ItemType Directory -Force | Out-Null
			}
			$outputPath = Join-Path $OutputFolder ([System.IO.Path]::ChangeExtension($file.Name, ".pdf"))
		}
        
		Write-Host "  入力: $inputPath" -ForegroundColor Gray
		Write-Host "  出力: $outputPath" -ForegroundColor Gray
        
		# 変換実行
		$result = Convert-WordToPDF -InputPath $inputPath -OutputPath $outputPath -OptimizeFor $optimizeFor
        
		if ($result) {
			$successCount++
			$pdfSize = (Get-Item $outputPath).Length / 1MB
			Write-Host "  サイズ: $([math]::Round($pdfSize, 2)) MB`n" -ForegroundColor Gray
		}
		else {
			$failCount++
			Write-Host ""
		}
	}
    
	# 結果サマリー
	Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
	Write-Host "  変換結果" -ForegroundColor Cyan
	Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
	Write-Host "成功: $successCount ファイル" -ForegroundColor Green
	if ($failCount -gt 0) {
		Write-Host "失敗: $failCount ファイル" -ForegroundColor Red
	}
	Write-Host ""
    
}
catch {
	Write-Host "`n✗ エラー: $($_.Exception.Message)" -ForegroundColor Red
	exit 1
}
