import cv2
import matplotlib.pyplot as plt
import numpy as np

# Đọc ảnh đầu vào
img = cv2.imread('C2_sanbay.tif')

# Xác định kích thước kernel (bộ lọc)
kernel_size = 5

# Tạo kernel bộ lọc trung bình
kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)

# Lọc mịn ảnh bằng bộ lọc trung bình
smoothed_img = cv2.filter2D(img, -1, kernel)
fig = plt.figure(figsize=(16, 9))

ax1, ax2 = fig.subplots(1, 2)

ax1.imshow(img)
ax1.set_title('Ảnh gốc')
ax2.imshow(smoothed_img)
ax2.set_title('Ảnh đã lọc mịn')

# Hiển thị ảnh
plt.show()
