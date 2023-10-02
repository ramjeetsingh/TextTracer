import cv2
import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('test.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)    #bcoz cv2 reads rgb images and pytesseract works with only bgr values

print(pytesseract.image_to_string(img))

myconfig = r"--psm 11 --oem 3"

# 2) to get boxes around words

data = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)
no_boxes = len(data['text'])

for i in range(no_boxes):
    if float(data['conf'][i]) > 80:                #if confidence is > 80
        (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        img = cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 2)
        img = cv2.putText(img, data['text'][i], (x, y + height + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

cv2.imshow('Result', img)
cv2.waitKey(0)