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

# 処理する画像ファイル名のリスト
filenames = [
    'a2-5_gray_image_0.png',
    'a2-5_gray_image_1.png',
    'a2-5_gray_image_2.png',
    'a2-5_gray_image_3.png',
    'a2-5_gray_image_4.png'
]

# フィルタ生成関数の定義
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

# 試行する遮断周波数リスト
cutoffs = [10, 30, 60]

# ループで各画像を個別に処理
for file_idx, filename in enumerate(filenames):
    # 画像読み込み
    gray_img = cv2.imread(common_path + filename, cv2.IMREAD_GRAYSCALE)

    # 画像サイズから最大の正方形サイズを決定してトリミング
    h, w = gray_img.shape
    crop_size = min(h, w)
    start_y = h // 2 - crop_size // 2
    start_x = w // 2 - crop_size // 2
    img = gray_img[start_y:start_y+crop_size, start_x:start_x+crop_size]

    # 2次元FFTとシフト
    fshift = np.fft.fftshift(np.fft.fft2(img))

    # 表示設定 (列数 = 遮断周波数の数)
    cols = len(cutoffs)
    plt.figure(figsize=(15, 8))
    plt.suptitle(f'Result for {filename}', fontsize=16)

    # --- 上段：理想ローパスフィルタ ---
    for i, d0 in enumerate(cutoffs):
        # マスク作成と適用
        mask_lp = create_ideal_lowpass(img.shape, d0)
        img_lp = np.fft.ifft2(np.fft.ifftshift(fshift * mask_lp)).real
        
        # 結果表示
        plt.subplot(2, cols, i + 1)
        plt.title(f'Ideal Low Pass (D0={d0})')
        plt.imshow(img_lp, cmap='gray')
        plt.axis('off')

    # --- 下段：ガウシアンハイパスフィルタ ---
    for i, d0 in enumerate(cutoffs):
        # マスク作成と適用
        mask_hp = create_gaussian_highpass(img.shape, d0)
        img_hp = np.fft.ifft2(np.fft.ifftshift(fshift * mask_hp)).real
        
        # 結果表示
        plt.subplot(2, cols, cols + i + 1)
        plt.title(f'Gaussian High Pass (D0={d0})')
        plt.imshow(np.abs(img_hp), cmap='gray')
        plt.axis('off')

    plt.tight_layout()

    # 画像を保存してダウンロード
    save_filename = f'problem2_4_result_{file_idx}.png'
    plt.savefig(save_filename)
    plt.show()
    files.download(save_filename)