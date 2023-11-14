import cv2
import pytesseract
from pytesseract import Output
import numpy as np

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


image = cv2.imread('test3.png')
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)             #bcoz cv2 reads rgb images and pytesseract works with only bgr values
thresh, binary = cv2.threshold(gray_image, 180, 255, cv2.THRESH_BINARY)


strct_element=cv2.getStructuringElement(cv2.MORPH_RECT , (5,5))
bg=cv2.morphologyEx(binary, cv2.MORPH_DILATE, strct_element)
img=cv2.divide(binary, bg, scale=255)


print(pytesseract.image_to_string(img))


myconfig = r"--psm 11 --oem 3"


data = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)
no_boxes = len(data['text'])


for i in range(no_boxes):
    if float(data['conf'][i]) > 50:                             #if confidence is > 50
        (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        img = cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 2)
        img = cv2.putText(img, data['text'][i], (x, y + height + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)


cv2.imshow('Result', img)
cv2.waitKey(0)





# Page segmentation modes:
#   0    Orientation and script detection (OSD) only.
#   1    Automatic page segmentation with OSD.
#   2    Automatic page segmentation, but no OSD, or OCR. (not implemented)
#   3    Fully automatic page segmentation, but no OSD. (Default)
#   4    Assume a single column of text of variable sizes.
#   5    Assume a single uniform block of vertically aligned text.
#   6    Assume a single uniform block of text.
#   7    Treat the image as a single text line.
#   8    Treat the image as a single word.
#   9    Treat the image as a single word in a circle.
#  10    Treat the image as a single character.
#  11    Sparse text. Find as much text as possible in no particular order.
#  12    Sparse text with OSD.
#  13    Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific.