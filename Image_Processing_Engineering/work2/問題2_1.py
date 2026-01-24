# -*- coding: utf-8 -*-
"""問題2_1.ipynb"""

# ドライブのマウントとファイル操作用モジュール
from google.colab import drive
from google.colab import files
drive.mount('/content/drive')

# モジュールのインポート
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

# 共通のディレクトリパス
common_path = '/content/drive/MyDrive/img2025/image/'
filename = 'a2-3_binary_image.png'

# 画像読み込み
img = cv2.imread(common_path + filename, cv2.IMREAD_GRAYSCALE)

# カーネルサイズのリスト
kernel_sizes = list(range(3, 17, 2))
total_images = 1 + len(kernel_sizes)

# レイアウト計算
cols = 4
rows = math.ceil(total_images / cols)

# 実行結果の表示設定
plt.figure(figsize=(15, 4 * rows))

# オリジナル画像
plt.subplot(rows, cols, 1)
plt.title('Original Image')
plt.imshow(img, cmap='gray')
plt.axis('off')

# カーネルサイズを変えて処理
for i, k in enumerate(kernel_sizes):
    # 1. 矩形カーネルでオープニング処理
    kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (k, k))
    img_rect = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel_rect)

    # 2. その結果に楕円カーネルでオープニング処理
    kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k, k))
    result = cv2.morphologyEx(img_rect, cv2.MORPH_OPEN, kernel_ellipse)

    # 表示
    plt.subplot(rows, cols, i + 2)
    plt.title(f'Rect->Ellipse (Size: {k}x{k})')
    plt.imshow(result, cmap='gray')
    plt.axis('off')

plt.tight_layout()

# 画像を保存してダウンロード
save_filename = 'problem2_1_rect_ellipse.png'
plt.savefig(save_filename)
plt.show()
files.download(save_filename)