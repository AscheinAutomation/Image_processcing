import cv2
import numpy as np

image = cv2.imread('barcelona.jpg', cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Không đọc được ảnh.")
else:
    kirsch1 = np.array([[5, 5, 5],
                        [-3, 0, -3],
                        [-3, -3, -3]])

    kirsch2 = np.array([[-3, -3, 5],
                        [-3, 0, 5],
                        [-3, -3, 5]])

    kirsch3 = np.array([[-3, -3, -3],
                        [-3, 0, -3],
                        [5, 5, 5]])

    kirsch4 = np.array([[5, -3, -3],
                        [5, 0, -3],
                        [5, -3, -3]])

    kirsch5 = np.array([[-3, -3, -3],
                        [5, 0, -3],
                        [5, 5, -3]])

    kirsch6 = np.array([[-3, 5, 5],
                        [-3, 0, 5],
                        [-3, -3, -3]])

    kirsch7 = np.array([[5, 5, 5],
                        [5, 0, -3],
                        [-3, -3, -3]])

    kirsch8 = np.array([[-3, 5, 5],
                        [-3, 0, 5],
                        [-3, -3, 5]])

    filtered_image1 = cv2.filter2D(image, -1, kirsch1)
    filtered_image2 = cv2.filter2D(image, -1, kirsch2)
    filtered_image3 = cv2.filter2D(image, -1, kirsch3)
    filtered_image4 = cv2.filter2D(image, -1, kirsch4)
    filtered_image5 = cv2.filter2D(image, -1, kirsch5)
    filtered_image6 = cv2.filter2D(image, -1, kirsch6)
    filtered_image7 = cv2.filter2D(image, -1, kirsch7)
    filtered_image8 = cv2.filter2D(image, -1, kirsch8)

    combined_image = np.maximum.reduce([filtered_image1, filtered_image2, filtered_image3,
                                        filtered_image4, filtered_image5, filtered_image6,
                                        filtered_image7, filtered_image8])

    resized_image = cv2.resize(image, None, fx=0.4, fy=0.4)
    resize_combine= cv2.resize(combined_image, None, fx=0.4, fy=0.4)
    cv2.imshow('Original Image', resized_image)
    cv2.imshow('Kirsch Edge Detection', resize_combine)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
