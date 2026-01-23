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
filename = 'a2-5_gray_image.png'

# 画像を読み込む
gray_img = cv2.imread(common_path + filename, cv2.IMREAD_GRAYSCALE)

# トリミング（512x512）
h, w = gray_img.shape
crop_size = 512
start_y = h // 2 - crop_size // 2
start_x = w // 2 - crop_size // 2
cropped_img = gray_img[start_y:start_y+crop_size, start_x:start_x+crop_size]

# 2次元FFTとシフト
fourier = np.fft.fft2(cropped_img)
fshift = np.fft.fftshift(fourier)

# 振幅スペクトル（対数スケール）
amp_spectrum = 20 * np.log10(np.abs(fshift) + 1)

# 実行結果の表示
plt.figure(figsize=(10, 5))

# トリミング画像
plt.subplot(1, 2, 1)
plt.title('Cropped Image')
plt.imshow(cropped_img, cmap='gray')
plt.axis('off')

# 振幅スペクトル
plt.subplot(1, 2, 2)
plt.title('Magnitude Spectrum (Log Scale)')
plt.imshow(amp_spectrum, cmap='gray')
plt.axis('off')

plt.tight_layout()

# 画像を保存してダウンロード
save_filename = 'problem2_3_result.png'
plt.savefig(save_filename)
plt.show()
files.download(save_filename)