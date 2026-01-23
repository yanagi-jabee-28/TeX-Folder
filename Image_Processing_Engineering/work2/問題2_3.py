# -*- coding: utf-8 -*-
"""問題2_3.ipynb"""

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

# ループで各画像を個別に処理・保存
for i, filename in enumerate(filenames):
    # 画像を読み込む
    gray_img = cv2.imread(common_path + filename, cv2.IMREAD_GRAYSCALE)

    # 画像サイズから最大の正方形サイズを決定
    h, w = gray_img.shape
    crop_size = min(h, w)

    # 中心から最大サイズでトリミング
    start_y = h // 2 - crop_size // 2
    start_x = w // 2 - crop_size // 2
    cropped_img = gray_img[start_y:start_y+crop_size, start_x:start_x+crop_size]

    # 2次元高速フーリエ変換（2D-FFT）
    fourier = np.fft.fft2(cropped_img)
    fshift = np.fft.fftshift(fourier)

    # 振幅スペクトル（対数スケール）
    amp_spectrum = 20 * np.log10(np.abs(fshift) + 1)

    # --- 表示と保存（1枚ずつ個別のFigureを作成） ---
    plt.figure(figsize=(10, 5))
    
    # 左側：トリミング画像
    plt.subplot(1, 2, 1)
    plt.title(f'{filename}\n(Size: {crop_size}x{crop_size})')
    plt.imshow(cropped_img, cmap='gray')
    plt.axis('off')

    # 右側：振幅スペクトル
    plt.subplot(1, 2, 2)
    plt.title('Magnitude Spectrum (Log Scale)')
    plt.imshow(amp_spectrum, cmap='gray')
    plt.axis('off')

    plt.tight_layout()

    # 個別に画像を保存してダウンロード
    save_filename = f'problem2_3_result_{i}.png'
    plt.savefig(save_filename)
    plt.show()
    files.download(save_filename)