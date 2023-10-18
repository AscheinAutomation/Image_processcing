import cv2
import matplotlib.pyplot as plt
import numpy as np

# Đọc ảnh đầu vào
img = cv2.imread('C2_sanbay.tif')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# kích thước kernel
kernel_size = 5
kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)

# Lọc mịn (lọc min) ảnh
smoothed_img = cv2.filter2D(gray_img, -1, kernel)

# Lọc nét (lọc max) ảnh
sharp_kernel = np.array([[0, -1, 0],
                         [-1, 5, -1],
                         [0, -1, 0]], np.float32)
sharp_img = cv2.filter2D(gray_img, -1, sharp_kernel)

fig = plt.figure(figsize=(16, 9))
(ax1, ax2), (ax3, ax4) = fig.subplots(2, 2)

ax1.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
ax1.set_title('Ảnh Gốc')

ax2.imshow(gray_img, cmap='gray')
ax2.set_title('Ảnh Xám')

ax3.imshow(smoothed_img, cmap='gray')
ax3.set_title('Ảnh Lọc Mịn (Lọc Min)')

ax4.imshow(sharp_img, cmap='gray')
ax4.set_title('Ảnh Lọc Nét (Lọc Max)')

plt.show()
