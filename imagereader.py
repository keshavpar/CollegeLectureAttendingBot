
from PIL.Image import new
import pytesseract as tess
import cv2
import time
import datetime
def dat():
        img = cv2.imread('kesh.png')
        shape =img.shape
        # print(shape[1])
        # newimg=img[ 400:600, 20:1000 ]     
        
        return img

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
days = datetime.datetime.today().weekday()
im = dat()
cv2.imshow("Image resized",im)
cv2.waitKey(100)
text = tess.image_to_string(im)
text = text.strip()
f = open('time.txt',"a")
f.write(text)
print(text)



    
# # if(day )




# # text = tess.image_to_string(img)
# # print(text)



# def dat():
#         img = cv2.imread('timetable.jpeg')
#         shape =img.shape
#         print(shape)
#         # newimg=img[0:l,b:]
