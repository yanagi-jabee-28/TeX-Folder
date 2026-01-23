# -*- coding: utf-8 -*-
"""問題2_4.ipynb"""

# ドライブのマウントとファイル操作用モジュール
from google.colab import drive
from google.colab import files
drive.mount('/content/drive')

# モジュールのインポート
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 共通のディレクトリパス
common_path = '/content/drive/MyDrive/img2025/image/'
filename = 'a2-5_gray_image.png'

# フィルタ生成関数
def create_ideal_lowpass(shape, cutoff):
    rows, cols = shape
    crow, ccol = rows // 2, cols // 2
    y, x = np.ogrid[:rows, :cols]
    dist_sq = (x - ccol)**2 + (y - crow)**2
    mask = np.zeros(shape)
    mask[dist_sq <= cutoff**2] = 1
    return mask

def create_gaussian_highpass(shape, cutoff):
    rows, cols = shape
    crow, ccol = rows // 2, cols // 2
    y, x = np.ogrid[:rows, :cols]
    dist_sq = (x - ccol)**2 + (y - crow)**2
    mask = 1 - np.exp(-dist_sq / (2 * (cutoff**2)))
    return mask

# 画像読み込みとトリミング
gray_img = cv2.imread(common_path + filename, cv2.IMREAD_GRAYSCALE)
h, w = gray_img.shape
size = 512
img = gray_img[h//2-size//2 : h//2+size//2, w//2-size//2 : w//2+size//2]

# 2次元FFTとシフト
fshift = np.fft.fftshift(np.fft.fft2(img))

# 試行する遮断周波数リスト
cutoffs = [10, 30, 60]

# 表示設定
cols = len(cutoffs) * 2
plt.figure(figsize=(18, 8))

# --- 上段：理想ローパスフィルタ ---
for i, d0 in enumerate(cutoffs):
    # マスク作成と適用
    mask_lp = create_ideal_lowpass(img.shape, d0)
    img_lp = np.fft.ifft2(np.fft.ifftshift(fshift * mask_lp)).real
    
    # マスク表示
    plt.subplot(2, cols, i * 2 + 1)
    plt.title(f'ILPF Mask (D0={d0})')
    plt.imshow(mask_lp, cmap='gray')
    plt.axis('off')

    # 結果表示
    plt.subplot(2, cols, i * 2 + 2)
    plt.title(f'Result (Low Pass)')
    plt.imshow(img_lp, cmap='gray')
    plt.axis('off')

# --- 下段：ガウシアンハイパスフィルタ ---
for i, d0 in enumerate(cutoffs):
    # マスク作成と適用
    mask_hp = create_gaussian_highpass(img.shape, d0)
    img_hp = np.fft.ifft2(np.fft.ifftshift(fshift * mask_hp)).real
    
    # マスク表示
    plt.subplot(2, cols, cols + i * 2 + 1)
    plt.title(f'GHPF Mask (D0={d0})')
    plt.imshow(mask_hp, cmap='gray')
    plt.axis('off')

    # 結果表示
    plt.subplot(2, cols, cols + i * 2 + 2)
    plt.title(f'Result (High Pass)')
    plt.imshow(np.abs(img_hp), cmap='gray')
    plt.axis('off')

plt.tight_layout()

# 画像を保存してダウンロード
save_filename = 'problem2_4_result.png'
plt.savefig(save_filename)
plt.show()
files.download(save_filename)