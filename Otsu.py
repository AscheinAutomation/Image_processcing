import cv2

image = cv2.imread('barcelona.jpg', cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Không đọc được ảnh.")
else:
    _, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    resized_image = cv2.resize(image, None, fx=0.4, fy=0.4)
    resize_otsu = cv2.resize(binary_image, None, fx=0.4, fy=0.4)
    cv2.imshow('Original Image', resized_image)
    cv2.imshow('Otsu Thresholded Image',resize_otsu)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
