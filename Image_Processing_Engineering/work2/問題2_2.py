# -*- coding: utf-8 -*-
"""問題2_2.ipynb"""

# ドライブのマウントとファイル操作用モジュール
from google.colab import drive
from google.colab import files
drive.mount('/content/drive')

# モジュールのインポート
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from skimage.metrics import structural_similarity as ssim

# 共通のディレクトリパス
common_path = '/content/drive/MyDrive/img2025/image/'
filename = 'a2-4_color_image.png'

# 画像を読み込む
original_img = cv2.imread(common_path + filename)
original_size = os.path.getsize(common_path + filename)
original_img_rgb = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)

# 画像表示の準備
plt.figure(figsize=(20, 15))

# 品質0から100まで10刻みでループ
for i, quality in enumerate(range(0, 101, 10)):
    # JPEG圧縮保存（一時ファイル）
    output_path = common_path + f'compressed_{quality}.jpg'
    cv2.imwrite(output_path, original_img, [int(cv2.IMWRITE_JPEG_QUALITY), quality])

    # 圧縮後のファイルサイズ取得と圧縮率計算
    comp_size = os.path.getsize(output_path)
    comp_ratio = (comp_size / original_size) * 100
    
    # 画像読み込み
    compressed_img = cv2.imread(output_path)
    compressed_img_rgb = cv2.cvtColor(compressed_img, cv2.COLOR_BGR2RGB)

    # SSIM計算
    score = ssim(original_img_rgb, compressed_img_rgb, win_size=3, channel_axis=2, data_range=255)

    # 表示
    plt.subplot(3, 4, i + 1)
    plt.imshow(compressed_img_rgb)
    plt.title(f"Q={quality}, Size={comp_ratio:.1f}%, SSIM={score:.3f}")
    plt.axis('off')

plt.tight_layout()

# 画像を保存してダウンロード
save_filename = 'problem2_2_result.png'
plt.savefig(save_filename)
plt.show()
files.download(save_filename)