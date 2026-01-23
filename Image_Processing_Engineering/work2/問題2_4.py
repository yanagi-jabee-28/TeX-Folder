# -*- coding: utf-8 -*-
"""問題2_4.ipynb"""

# ドライブのマウント
from google.colab import drive
drive.mount('/content/drive')

# モジュールのインポート
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 共通のディレクトリパス
common_path = '/content/drive/MyDrive/img2025/image/'
filename = 'a2-5_gray_image.png'

# フィルタ生成関数の定義
def create_filter(shape, filter_type, cutoff):
    rows, cols = shape
    crow, ccol = rows // 2, cols // 2
    y, x = np.ogrid[:rows, :cols]
    # 中心からの距離の二乗
    dist_sq = (x - ccol)**2 + (y - crow)**2
    
    mask = np.zeros(shape)
    if filter_type == 'low':
        # 理想ローパスフィルタ
        mask[dist_sq <= cutoff**2] = 1
    elif filter_type == 'high':
        # ガウシアンハイパスフィルタ
        mask = 1 - np.exp(-dist_sq / (2 * (cutoff**2)))
        
    return mask

# 画像読み込み
gray_img = cv2.imread(common_path + filename, cv2.IMREAD_GRAYSCALE)

# トリミング（512x512）
h, w = gray_img.shape
size = 512
img = gray_img[h//2-size//2 : h//2+size//2, w//2-size//2 : w//2+size//2]

# FFTとシフト
fshift = np.fft.fftshift(np.fft.fft2(img))

# フィルタリングパラメータ
cutoff = 30

# 1. 理想ローパスフィルタの適用
mask_low = create_filter(img.shape, 'low', cutoff)
fshift_low = fshift * mask_low
img_low = np.fft.ifft2(np.fft.ifftshift(fshift_low)).real

# 2. ガウシアンハイパスフィルタの適用
mask_high = create_filter(img.shape, 'high', cutoff)
fshift_high = fshift * mask_high
img_high = np.fft.ifft2(np.fft.ifftshift(fshift_high)).real

# 結果の表示
plt.figure(figsize=(12, 8))

# 上段：ローパスフィルタ
plt.subplot(2, 3, 1)
plt.title('Original Image')
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.title('Ideal Low Pass Mask')
plt.imshow(mask_low, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.title('Result (Low Pass)')
plt.imshow(img_low, cmap='gray')
plt.axis('off')

# 下段：ハイパスフィルタ
plt.subplot(2, 3, 4)
plt.title('Original Image')
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.title('Gaussian High Pass Mask')
plt.imshow(mask_high, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 6)
plt.title('Result (High Pass)')
plt.imshow(np.abs(img_high), cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()