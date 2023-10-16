import cv2
import matplotlib.pyplot as plt

def Chuyendoi_Logarit(img, c):
    return float(c) * cv2.log(1.0 + img)

def show_logarit():
    fig = plt.figure(figsize=(16,9))
    (ax1, ax2), (ax3, ax4) = fig.subplots(2, 2)

    img = cv2.imread("C2_sanbay.tif", 0)
    ax1.imshow(img, cmap='gray')
    ax1.set_title("anh goc")

    y1 = Chuyendoi_Logarit(img, 2)
    ax2.imshow(y1, cmap='gray')
    ax2.set_title("Anh Chuyen doi Logarit 1")

    y2 = Chuyendoi_Logarit(img, 1.5)
    ax3.imshow(y2, cmap='gray')
    ax3.set_title("Anh Chuyen doi Logarit 2")

    y3 = Chuyendoi_Logarit(img, 1)
    ax4.imshow(y3, cmap='gray')
    ax4.set_title("Anh Chuyen doi Logarit 3")

    plt.show()
    # hàm plt.show sẽ chỉ được gọi 1 lần duy nhất và đặt ở cuối hàm định nghĩa để thể hiện toàn bộ các trục
if __name__ == '__main__':
    show_logarit()


