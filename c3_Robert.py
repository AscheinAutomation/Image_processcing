import cv2
import numpy as np
from scipy import ndimage

def show_robert():
    roberts_cross_v = np.array([[1, 0],
                                [0, -1]])

    roberts_cross_h = np.array([[0, 1],
                                [-1, 0]])

    img = cv2.imread("test2.tif", 0).astype('float64')
    img /= 255.0
    vertical = ndimage.convolve(img, roberts_cross_v)
    horizontal = ndimage.convolve(img, roberts_cross_h)

    edged_img = np.sqrt(np.square(horizontal) + np.square(vertical))
    edged_img *= 255
    cv2.imwrite("output.jpg", edged_img)
    cv2.imshow("output", edged_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    show_robert()