import cv2
import numpy as np
import matplotlib.pyplot as plt

gray_image = cv2.imread('barcelona.jpg', cv2.IMREAD_GRAYSCALE)

height, width = gray_image.shape
depth = gray_image.dtype

print(f'Chiều cao: {height} pixels')
print(f'Chiều rộng: {width} pixels')
print(f'Độ sâu: {depth} bits per pixel')

muoi_tieu = np.zeros_like(gray_image)
probability = 0.5  # Điều chỉnh xác suất xuất hiện nhiễu muối tiêu

for i in range(gray_image.shape[0]):
    for j in range(gray_image.shape[1]):
        rand = np.random.rand()
        if rand < probability / 2:
            muoi_tieu[i, j] = 0  # Muối
        elif rand < probability:
            muoi_tieu[i, j] = 255  # Tiêu

anh_moi = cv2.add(gray_image, muoi_tieu.astype(np.uint8))

kernel_size = 5
anh_loctrungbinh = cv2.blur(anh_moi, (kernel_size, kernel_size))

bien = cv2.Canny(anh_loctrungbinh, 50, 150)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(cv2.cvtColor(anh_loctrungbinh, cv2.COLOR_BGR2RGB))
axes[0].set_title('Ảnh sau khi Lọc trung bình')

axes[1].imshow(bien, cmap='gray')
axes[1].set_title('Biên Ảnh (Canny)')

plt.show()
