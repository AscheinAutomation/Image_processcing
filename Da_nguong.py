import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh đầu vào
img = cv2.imread('wallpaperflare.com_wallpaper.jpg', 0)

# Đặt các ngưỡng cần dùng
thresholds = [100, 150, 200]

# Tạo mảng để lưu kết quả phân đoạn
segmented_images = []

for threshold in thresholds:
    # Áp dụng ngưỡng cho ảnh
    ret, segmented = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    segmented_images.append(segmented)

# Tạo vùng vẽ
fig, axes = plt.subplots(1, len(thresholds) + 1, figsize=(16, 9))

axes[0].imshow(img, cmap='gray')
axes[0].set_title('Ảnh Xám')

for i, threshold in enumerate(thresholds):
    axes[i + 1].imshow(segmented_images[i], cmap='gray')
    axes[i + 1].set_title(f'Ngưỡng {threshold}')

plt.show()
