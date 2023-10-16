import cv2
import matplotlib.pyplot as plt

img = cv2.imread('keodan_dau.tif', 0)
img_equalized = cv2.equalizeHist(img)

fig = plt.figure(figsize=(16,9))
(ax1, ax2), (ax3, ax4) = fig.subplots(2,2)

ax1.imshow(img, cmap='gray')
ax1.set_title("Anh goc")

# Vẽ Hist của ảnh gốc trong vùng ax2
ax2.hist(img)
ax2.set_title("Histogram cuar anhr goc")

# Vẽ ảnh sau khi cân bằng Hist trong vùng ax3
ax3.imshow(img_equalized, cmap='gray')
ax3.set_title("ảnh cân bằng histogram")

# Vẽ hist của ảnh cân bằng hist trong vùng ax4
ax4.hist(img_equalized)
ax4.set_title("Histogram ảnh cân bằng")

plt.show() # Hiển thị vùng vẽ