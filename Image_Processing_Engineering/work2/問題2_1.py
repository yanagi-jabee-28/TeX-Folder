# -*- coding: utf-8 -*-
"""問題2_1.ipynb"""

# ドライブのマウント
from google.colab import drive
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

# カーネルサイズのリスト（3から15まで2ずつ増やす）
# 学生がパラメータを変えて試行錯誤した様子
kernel_sizes = list(range(3, 17, 2))
total_images = 1 + len(kernel_sizes)

# レイアウト計算
cols = 4
rows = math.ceil(total_images / cols)

# 実行結果の表示
plt.figure(figsize=(15, 4 * rows))

# オリジナル画像
plt.subplot(rows, cols, 1)
plt.title('Original Image')
plt.imshow(img, cmap='gray')
plt.axis('off')

# カーネルサイズを変えて処理
for i, k in enumerate(kernel_sizes):
    # カーネル作成（矩形）
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (k, k))
    
    # オープニング処理（収縮→膨張）でノイズ除去
    result = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    
    # 表示
    plt.subplot(rows, cols, i + 2)
    plt.title(f'Opening (Kernel: {k}x{k})')
    plt.imshow(result, cmap='gray')
    plt.axis('off')

plt.tight_layout()
plt.show()