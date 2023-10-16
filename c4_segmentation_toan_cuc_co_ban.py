# Phân đoạn ảnh bằng cắt ngưỡng được với ngưỡng tìm được
# bằng thuật toán tìm ngưỡng toàn cục cơ bản
import cv2
import numpy as np
from matplotlib import pyplot as plt


# Định nghĩa hàm tìm ngưỡng
def Tim_nguong_toan_cuc(img):  # Định nghĩa hàm tìm ngưỡng

    # Bước 1. Khởi tạo ngưỡng ban đầu t bằng giá trị trung bình mức xám của ảnh
    t = np.mean(img)  # Khoi tao dieu kien ban dau
    g1 = []  # Định nghĩa nhóm G1
    g2 = []  # Định nghĩa nhóm G2
    m, n = img.shape
    # Lặp để tính ngưỡng
    while (True):
        # Bước 2. Tạo nhóm G1,G2 dựa trên ngưỡng t
        for i in range(m):
            for j in range(n):
                if (img[i, j] < t):
                    g1.append(img[i, j])
                else:
                    g2.append(img[i, j])

        # Bước 3. Tính trung bình mức xám trong vùng G1,G2
        mu1 = np.mean(g1)
        mu2 = np.mean(g2)

        # Bước 4. Tính lại ngưỡng t có giá trị mới
        t = ((mu1 + mu2) / 2)
        # Tính delta t để làm điều kiện thoát vòng lặp
        t0 = t
        delta_t = abs(t - t0)
        if (delta_t < 1):
            break
    print("Ngưỡng tìm được: ", t)
    return t


# Định nghĩa hàm phân đoạn bằng cắt ngưỡng
def phan_doan_bang_cat_nguong(img, nguong):
    m, n = img.shape
    img_phan_doan_cat_nguong = np.zeros([m, n])
    for i in range(m):
        for j in range(n):
            if (img[i, j] < nguong):
                img_phan_doan_cat_nguong[i, j] = 0
            else:
                img_phan_doan_cat_nguong[i, j] = 225  # tương đương giá trị 1 trong trong công thức
    return img_phan_doan_cat_nguong


if __name__ == "__main__":
    # reading image in gray scale
    img_goc = cv2.imread("C4_thanh.tif", 0)

    # gọi ham để phân đoạn bằng cắt ngưỡng toàn cục dựa trên ngưỡng
    T = Tim_nguong_toan_cuc(img_goc)
    img_phan_doan = phan_doan_bang_cat_nguong(img_goc, T)

    # Vẽ và hiển thị ảnh gốc, histogram ảnh gốc và ảnh phân đoạn
    fig2 = plt.figure(figsize=(16, 9))  # Tạo vùng vẽ tỷ lệ 16:9

    # Tạo 4 vùng vẽ con
    (ax1, ax2), (ax3, ax4) = fig2.subplots(2, 2)

    # Hiển thị ảnh gốc
    ax1.imshow(img_goc, cmap='gray')
    ax1.set_title('Ảnh gốc')
    ax1.axis('off')

    # Hiển thị histogram ảnh gốc
    ax2.hist(img_goc.flatten(), bins=256)
    ax2.set_title('Hitogram ảnh gốc')

    # Hiển thị ảnh phân đoạn
    ax3.imshow(img_phan_doan, cmap='gray')
    ax3.set_title('Ảnh phân đoạn dựa vào tìm ngưỡng cơ bản')
    ax3.axis('off')

    # Hiển thị histogram ảnh phân đoạn
    ax4.hist(img_phan_doan.flatten(), bins=256)
    ax4.set_title('Hitogram ảnh phân đoạn')
    plt.show()
