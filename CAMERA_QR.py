from pickle import TRUE
import cv2
import numpy
import sys
import statistics

#Define global variables
t = 1
Areas = []
Radio = []
Centers = []
video = cv2.VideoCapture(1)
detector = cv2.QRCodeDetector()
path = r'C:/git/VISION/image.jpg'


while(t == 1):

    #Generamos el video de la camara 1
    ret, frame = video.read()
    cv2.imshow('frame', frame)
    k = cv2.waitKey(1) & 0xFF

    if k == ord('t'):
        cv2.imwrite(path,frame)
        print("ENTRE A TOMAR FOTO")


    if k == ord ('a'):
        img = cv2.imread(path)
        gauss = cv2.GaussianBlur(img, (5,5), 0)
        median = cv2.medianBlur(img,5)
        canny1 = cv2.Canny(img, 100, 150)
        canny2 = cv2.dilate(canny1, None, iterations=1)
        canny3 = cv2.erode(canny2, None, iterations=1)
        cnts,_ = cv2.findContours(canny3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)# OpenCV 4
        print("He encontrado {} objetos".format(len(cnts)))
    
        for c in cnts:
            area = cv2.contourArea(c)
            Areas.append(area)
            (x,y),radius = cv2.minEnclosingCircle(c)
            Radio.append(int(radius))
            if(area > 50000):
                x,y,w,h = cv2.boundingRect(c)
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        
        print(Areas)
        cv2.imshow("Foto proceso",img)
            


    if k == ord ('c'):
        t = 2 
        break

video.release()
cv2.destroyAllWindows()
