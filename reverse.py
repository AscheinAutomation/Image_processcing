import cv2
import matplotlib.pyplot as plt

# Đọc ảnh đầu vào
img = cv2.imread('wallpaperflare.com_wallpaper.jpg')

# Đảo ngược màu của tất cả các kênh màu
inverted_img = cv2.bitwise_not(img)

# Tạo vùng vẽ
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9))

# Hiển thị ảnh gốc
ax1.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# cvtColor là hàm chuyển đổi màu, matplot sử dụng thư viện RGB còn Opencv đọc ảnh bằng thư viện BGR, nên sẽ là BGR "to" RGB
ax1.set_title('Ảnh gốc')

# Hiển thị ảnh âm bản
ax2.imshow(cv2.cvtColor(inverted_img, cv2.COLOR_BGR2RGB))
ax2.set_title('Ảnh âm bản')

# Hiển thị ảnh gốc và ảnh âm bản
plt.show()
