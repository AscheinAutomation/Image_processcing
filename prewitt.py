import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('C2_sanbay.tif', cv2.IMREAD_GRAYSCALE)

# Tạo kernel Prewitt cho việc tính đạo hàm theo trục X
kernel_x = np.array([[-1, 0, 1],
                     [-1, 0, 1],
                     [-1, 0, 1]], dtype=np.float32)

# Tạo kernel Prewitt cho việc tính đạo hàm theo trục Y
kernel_y = np.array([[-1, -1, -1],
                     [0, 0, 0],
                     [1, 1, 1]], dtype=np.float32)

prewitt_x = cv2.filter2D(img, -1, kernel_x)
prewitt_y = cv2.filter2D(img, -1, kernel_y)

# Kết hợp đạo hàm theo trục X và Y để tính đạo hàm gradient
gradient_magnitude = np.sqrt(prewitt_x ** 2 + prewitt_y ** 2)

fig = plt.figure(figsize=(16, 9))
(ax1, ax2, ax3) = fig.subplots(1, 3)

ax1.imshow(img, cmap='gray')
ax1.set_title('Ảnh Gốc')

ax2.imshow(prewitt_x, cmap='gray')
ax2.set_title('Đạo hàm theo trục X')

ax3.imshow(gradient_magnitude, cmap='gray')
ax3.set_title('Đạo hàm Gradient')

plt.show()
