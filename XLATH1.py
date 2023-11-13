import cv2
import numpy as np
import matplotlib.pyplot as plt

gray_image = cv2.imread('barcelona.jpg', cv2.IMREAD_GRAYSCALE)

height, width = gray_image.shape
depth = gray_image.dtype

print(f'Chiều cao: {height} pixels')
print(f'Chiều rộng: {width} pixels')
print(f'Độ sâu: {depth} bits per pixel')

mean = 0
sigma = 25
gauss_noise = np.random.normal(mean, sigma, gray_image.shape)

anh_moi = cv2.add(gray_image, gauss_noise.astype(np.uint8))

anh_loctrungvi = cv2.medianBlur(anh_moi, 5)

bien = cv2.Canny(anh_loctrungvi, 50, 150)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(cv2.cvtColor(anh_loctrungvi, cv2.COLOR_BGR2RGB))
axes[0].set_title('Ảnh sau khi Lọc Trung Vị')

axes[1].imshow(bien, cmap='gray')
axes[1].set_title('Biên Ảnh (Canny)')

plt.show()
