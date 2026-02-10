param(
	[string]$InputTex = "Yanagihara_BCDR_MEGTRON6_2026.tex",
	[string]$OutputDocx = "Yanagihara_BCDR_MEGTRON6_2026.docx",
	[string]$WorkingDir = "$PSScriptRoot\.."
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -Path $WorkingDir)) {
	throw "WorkingDir not found: $WorkingDir"
}

Push-Location $WorkingDir
try {
	if (-not (Test-Path -Path $InputTex)) {
		throw "Input .tex not found: $InputTex"
	}

	$tex2docxCmd = Get-Command tex2docx -ErrorAction SilentlyContinue
	if (-not $tex2docxCmd) {
		throw "tex2docx not found. Install with: pip install tex2docx"
	}

	Write-Host "Converting $InputTex -> $OutputDocx" -ForegroundColor Cyan
	tex2docx convert --input-texfile $InputTex --output-docxfile $OutputDocx
	Write-Host "Done: $OutputDocx" -ForegroundColor Green
}
finally {
	Pop-Location
}
