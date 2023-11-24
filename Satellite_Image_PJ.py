import cv2
import numpy as np
import matplotlib.pyplot as plt


# Hàm chuyển đổi ảnh màu thành ảnh màu phân biệt độ cao với màu sắc tùy chỉnh
def convert_to_custom_colormap(input_image):
    # Lấy ảnh độ cao hoặc thông tin độ cao từ ảnh đầu vào (giả sử độ cao là kênh màu xám)
    height_image = input_image  # Không cần chỉ đến kênh, vì ảnh đã là ảnh xám

    # Chọn colormap (ví dụ: 'viridis') và ánh xạ giá trị độ cao thành giá trị màu tương ứng
    colormap = plt.get_cmap('viridis')
    height_colormap = (colormap(height_image) * 255).astype(np.uint8)

    # Tạo một mảng trắng với kích thước giống với ảnh đầu vào
    custom_colormap = np.zeros_like(height_colormap)

    # Tùy chỉnh giá trị màu sắc: đỏ thành xanh lá, xanh dương thành vàng đậm
    custom_colormap[:, :, :2] = height_colormap[:, :, 1:3]  # Sử dụng kênh màu xanh lá và vàng đậm

    return custom_colormap


# Tải ảnh vệ tinh (ảnh độ cao)
input_image = cv2.imread('VT1.png', cv2.IMREAD_GRAYSCALE)

# Gọi hàm chuyển đổi ảnh và lưu ảnh đầu ra
output_image = convert_to_custom_colormap(input_image)
cv2.imwrite('output_custom_colormap_image.jpg', output_image)

# Hiển thị ảnh đầu ra
cv2.imshow('Custom Colormap Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
