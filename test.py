import cv2
import numpy as np
import pytesseract as pt

image = cv2.imread('test5.jpg')
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

strct_element=cv2.getStructuringElement(cv2.MORPH_RECT , (8,8))
bg=cv2.morphologyEx(gray_image, cv2.MORPH_DILATE, strct_element)
im_gray=cv2.divide(gray_image, bg, scale=255)

kernel = np.ones((1,1), np.uint8)
result = cv2.dilate(im_gray, kernel, iterations=1)

cv2.imshow('res', result)
cv2.waitKey(0)

# ocr_result = pt.image_to_string(no_noise)
# print(ocr_result)

