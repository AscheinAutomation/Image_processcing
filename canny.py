import cv2

image = cv2.imread('barcelona.jpg', cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Không đọc được ảnh.")
else:
    edges = cv2.Canny(image, 100, 200)

    resized_image = cv2.resize(image, None, fx=0.4, fy=0.4)
    resize_edges = cv2.resize(edges, None, fx=0.4, fy=0.4)
    cv2.imshow('Original Image', resized_image)
    cv2.imshow('Canny Edge Detection', resize_edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
