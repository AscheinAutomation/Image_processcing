import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh đầu vào
img = cv2.imread('C2_sanbay.tif', 0)

# Tạo kernel Laplacian
kernel = np.array([[0, 1, 0],
                   [1, -4, 1],
                   [0, 1, 0]], dtype=np.float32)

laplacian = cv2.filter2D(img, -1, kernel)

fig = plt.figure(figsize=(16, 9))
(ax1, ax2) = fig.subplots(1, 2)

ax1.imshow(img, cmap='gray')
ax1.set_title('Ảnh Gốc')

ax2.imshow(laplacian, cmap='gray')
ax2.set_title('Đạo hàm Laplacian')

plt.show()
