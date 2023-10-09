import cv2
import numpy as np

def Tich_chap(img, mask):
    m, n = img.shape
    img_new = np.zeros([m, n])
    for i in range(1, m-1):
        for j in range(1, n-1):
            temp = img[i-1, j-1] * mask[0, 0]\
                + img[i-1, j] * mask[0, 1]\
                + img[i-1, j+1] * mask[0, 2]\
                + img[i, j-1] * mask[1, 0]\
                + img[i, j] * mask[1, 1]\
                + img[i, j+1] * mask[1, 2]\
                + img[i+1, j-1] * mask[2, 0]\
                + img[i+1, j] * mask[2, 1]\
                + img[i + 1, j + 1] * mask[2, 2]
            img_new[i, j] = temp
    img_new = img_new.astype(np.uint8)
    return img_new

image = cv2.imread('TTD_1014.JPG', cv2.IMREAD_GRAYSCALE)

kernel = np.array([[1, -2, 1],
                   [1, 1, 1],
                   [1, -2, 1]])


result = Tich_chap(image, kernel)
image_re = cv2.resize(image, None, fx=0.15, fy=0.15)
result_re = cv2.resize(result, None, fx=0.15, fy=0.15)
cv2.imshow('Original Image', image_re)
cv2.imshow('Convolution Result', result_re)

cv2.waitKey(0)
cv2.destroyAllWindows()
