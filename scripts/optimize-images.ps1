<#
Optimize images in the `image/` folder and write downsized copies to `image/optimized/`.
Requirements: ImageMagick (magick). Run in PowerShell:
  ./optimize-images.ps1 [-MaxSize 1600] [-Quality 85]
#>
param(
	[int] $MaxSize = 1600,
	[int] $Quality = 85,
	[switch] $Force,
	[string] $TargetDir
)

# Try to find repo root (parent of scripts) and image dir. If TargetDir provided, use it.
$repoRoot = Split-Path -Parent $PSScriptRoot
if ($TargetDir) {
	$imageDir = Resolve-Path -LiteralPath $TargetDir -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Path -ErrorAction SilentlyContinue
}
else {
	$imageDir = Join-Path $repoRoot "Experiment\9_高周波線路\image"
	if (-not (Test-Path $imageDir)) {
		# try to locate directory automatically (handles non-ascii path variations)
		$imageDirs = Get-ChildItem -Path $repoRoot -Directory -Recurse -ErrorAction SilentlyContinue | Where-Object { $_.Name -ieq 'image' }
		# Prefer image dirs that are under a folder containing '9_' (the assignment folder)
		$pref = $imageDirs | Where-Object { $_.FullName -match '9_' }
		if ($pref -and $pref.Count -gt 0) { $imageDir = $pref[0].FullName }
		elseif ($imageDirs -and $imageDirs.Count -gt 0) { $imageDir = $imageDirs[0].FullName }
		else { $imageDir = $null }
	}
}
$optimizedDir = Join-Path $imageDir "optimized"
if (-not (Test-Path $imageDir)) {
	Write-Error "image directory not found: $imageDir"
	exit 1
}
if (-not (Test-Path $optimizedDir)) { New-Item -ItemType Directory -Path $optimizedDir | Out-Null }
# Find images
$patterns = @('*.png', '*.jpg', '*.jpeg', '*.tif', '*.tiff')
$images = foreach ($p in $patterns) { Get-ChildItem -Path $imageDir -Filter $p -File -ErrorAction SilentlyContinue }
if ($images.Count -eq 0) { Write-Output "No images found in $imageDir"; exit 0 }
# Check ImageMagick
$magick = Get-Command magick -ErrorAction SilentlyContinue
if (-not $magick) {
	Write-Error "ImageMagick 'magick' not found in PATH. Install ImageMagick or use another tool."
	exit 2
}
foreach ($img in $images) {
	$src = $img.FullName
	$dst = Join-Path $optimizedDir $img.Name
	if (-not $Force -and (Test-Path $dst) -and ((Get-Item $dst).LastWriteTime -ge $img.LastWriteTime)) {
		Write-Output "Up-to-date: $($img.Name)"
		continue
	}
	# Use magick to resize only if larger than MaxSize (keep aspect ratio)
	Write-Output "Optimizing: $($img.Name) -> optimized/"
	try {
		& magick "$src" -resize "${MaxSize}x${MaxSize}>" -strip -quality $Quality "$dst"
	}
 catch {
		Write-Warning "Failed to optimize $src : $_"
	}
}
Write-Output "Optimization complete. Optimized images are in: $optimizedDir"