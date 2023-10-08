import cv2

image = cv2.imread('TTD_1014.JPG')

# scale_factor_x = 0.15
# scale_factor_y = 0.15

resized_image = cv2.resize(image, None, fx=0.15, fy=0.15)

cv2.imshow('Resized_image',resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
