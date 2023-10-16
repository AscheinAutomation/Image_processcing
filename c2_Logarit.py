import cv2
import matplotlib.pyplot as plt

def Chuyendoi_Logarit(img, c):
    return float(c) * cv2.log(1.0 + img)

def show_logarit():
    fig = plt.figure(figsize=(16,9))
    ax1, ax2 = fig.subplots(1, 2)

    img = cv2.imread("C2_logarit_2.jpg", 0)
    ax1.imshow(img, cmap='gray')
    ax1.set_title("anh goc")

    y = Chuyendoi_Logarit(img, 2)
    ax2.imshow(y, cmap='gray')
    ax2.set_title("Anh Chuyen doi Logarit")
    plt.show()

if __name__ == '__main__':
    show_logarit()


