import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh và chuyển đổi sang ảnh grayscale
image = cv2.imread('barcelona.jpg')
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Phương pháp region growing
seed_point = (100, 100)  # Điểm gốc
region_threshold = 30  # Ngưỡng region
region_mask = np.zeros_like(grayImage, dtype=np.uint8)
visited = np.zeros_like(grayImage, dtype=np.uint8)


def region_growing(image, seed, threshold):
    h, w = image.shape[:2]
    visited[seed] = 255
    region_mask[seed] = 255
    stack = [seed]

    while stack:
        current_pixel = stack.pop()
        neighbors = [
            (current_pixel[0] - 1, current_pixel[1]),
            (current_pixel[0] + 1, current_pixel[1]),
            (current_pixel[0], current_pixel[1] - 1),
            (current_pixel[0], current_pixel[1] + 1)
        ]

        for neighbor in neighbors:
            x, y = neighbor
            if x >= 0 and x < h and y >= 0 and y < w:
                if visited[x, y] == 0 and abs(int(image[x, y]) - int(image[current_pixel])) <= threshold:
                    visited[x, y] = 255
                    region_mask[x, y] = 255
                    stack.append((x, y))


region_growing(grayImage, seed_point, region_threshold)

# Erosion
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(region_mask, kernel, iterations=1)

# Dilation
dilation = cv2.dilate(region_mask, kernel, iterations=1)

# Opening
opening = cv2.morphologyEx(region_mask, cv2.MORPH_OPEN, kernel)

# Closing
closing = cv2.morphologyEx(region_mask, cv2.MORPH_CLOSE, kernel)

# Tạo một subplot grid 2 hàng x 3 cột cho việc hiển thị 5 ảnh
fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, figsize=(16, 9))

# Hiển thị ảnh gốc và các kết quả
ax1.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
ax1.set_title("Ảnh Gốc")

ax2.imshow(region_mask, cmap='gray')
ax2.set_title("Region Mask")

ax3.imshow(erosion, cmap='gray')
ax3.set_title("Erosion")

ax4.imshow(dilation, cmap='gray')
ax4.set_title("Dilation")

ax5.imshow(opening, cmap='gray')
ax5.set_title("Opening")

ax6.imshow(closing, cmap='gray')
ax6.set_title("Closing")

# Hiển thị tất cả ảnh trên cùng một đồ thị
plt.show()
