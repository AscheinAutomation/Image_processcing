import cv2
import matplotlib.pyplot as plt

def show_Histogram():
    # thường sẽ xảy ra lỗi indent unexpected tại vị trí này, vì ta định nghĩa một hàm nhưng không lùi các phần tử của hàm về đúng vị trí
    img = cv2.imread('C2_sanbay.tif', 0)
    # flag:0 nghĩa là ta thông báo cho chương trình biết rằng ta muốn đọc ảnh ở chế độ ảnh xám
    img_equalized = cv2.equalizeHist(img)
    # hàm cv2.equalizeHist là hàm cân bằng histogram
    fig = plt.figure(figsize=(16,9))
    (ax1, ax2), (ax3, ax4) = fig.subplots(2,2)

    ax1.imshow(img, cmap='gray')
    ax1.set_title("Anh goc")

    # Vẽ Hist của ảnh gốc trong vùng ax2
    ax2.hist(img)
    ax2.set_title("Histogram cua anh goc")

    # Vẽ ảnh sau khi cân bằng Hist trong vùng ax3
    ax3.imshow(img_equalized, cmap='gray')
    ax3.set_title("ảnh cân bằng histogram")

    # Vẽ hist của ảnh cân bằng hist trong vùng ax4
    ax4.hist(img_equalized)
    ax4.set_title("Histogram ảnh cân bằng")

    plt.show() # Hiển thị vùng vẽ

if __name__ == '__main__':
    show_Histogram()
