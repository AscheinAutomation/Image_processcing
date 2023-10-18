import cv2
from matplotlib import pyplot as plt

# Đọc ảnh xám
img = cv2.imread('barcelona.jpg', 0)

# Áp dụng cắt ngưỡng cố định
threshold_value = 128
thresholded_img = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)

# Hiển thị ảnh gốc và ảnh cắt ngưỡng

fig = plt.figure(figsize=(16, 9))
ax1, ax2 = fig.subplots(1, 2)
ax1.imshow(img, cmap='gray')
ax1.set_title('Ảnh gốc')

ax2.imshow(thresholded_img, cmap='gray')
ax2.set_title('Ảnh sau cắt ngưỡng')

plt.show()
