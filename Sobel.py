import cv2
import matplotlib.pyplot as plt

# Đọc ảnh đầu vào
img = cv2.imread('C2_sanbay.tif', 0)

# Áp dụng bộ lọc Sobel
sobel_result = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=5)
# cv2.CV_64F là kiểu dữ liệu đầu ra cho đạo hàm

fig = plt.figure(figsize=(16, 9))
(ax1, ax2) = fig.subplots(1, 2)

ax1.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
ax1.set_title('Ảnh Gốc')

ax2.imshow(cv2.convertScaleAbs(sobel_result), cmap='gray')
ax2.set_title('Kết Quả Sobel')

plt.show()
