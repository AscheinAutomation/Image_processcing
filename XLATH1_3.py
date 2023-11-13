import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('barcelona.jpg')
gr_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_equalized = cv2.equalizeHist(gr_img)
# hàm cv2.equalizeHist là hàm cân bằng histogram

kernel_kirsch_1 = np.array([[-3, -3, -3], [-3, 0, -3], [5, 5, 5]])
kernel_kirsch_2 = np.array([[-3, -3, 5], [-3, 0, 5], [-3, -3, 5]])
kernel_kirsch_3 = np.array([[-3, 5, 5], [-3, 0, 5], [-3, -3, -3]])
kernel_kirsch_4 = np.array([[5, 5, 5], [-3, 0, -3], [-3, -3, -3]])

kirsch_1 = cv2.filter2D(gr_img, -1, kernel_kirsch_1)
kirsch_2 = cv2.filter2D(gr_img, -1, kernel_kirsch_2)
kirsch_3 = cv2.filter2D(gr_img, -1, kernel_kirsch_3)
kirsch_4 = cv2.filter2D(gr_img, -1, kernel_kirsch_4)

kirsch_qua = cv2.add(cv2.add(cv2.add(kirsch_1, kirsch_2), kirsch_3), kirsch_4)

fig = plt.figure(figsize=(16, 9))
(ax1, ax2), (ax3, ax4) = fig.subplots(2, 2)

ax1.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), cmap='gray')
ax1.set_title("Anh goc")

# Vẽ Hist của ảnh gốc trong vùng ax2
ax2.hist(gr_img)
ax2.set_title("Histogram cua anh goc")

ax3.imshow(gr_img, cmap='gray')
ax3.set_title("Anh xam")

ax4.imshow(np.abs(kirsch_qua), cmap='gray')
ax4.set_title("bien Kirsch")
plt.show()
