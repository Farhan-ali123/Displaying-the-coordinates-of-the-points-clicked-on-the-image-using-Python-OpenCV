import cv2 as cv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

[print(i) for i in dir(cv) if 'EVENT' in i]
def click_event(event,x,y,flags,params):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x , ' ' , y)
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img, str(x) + ',' + str(y) ,(x,y) , font , 1 , (255,0,0) , 2 )
        cv.imshow('image', img )
    if event ==cv.EVENT_RBUTTONDOWN:
        print(x , ' ' , y)
        font = cv.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv.putText(img , str(b) + ',' + str(g) + ',' + str(r) , font , 1 , (255,255,0) , 2 )
        cv.imshow('image' , img)
if __name__ =="__main__":
    img = cv.imread('C:\\Users\\user\\Desktop\\newp\\venv\\resources\\lena.jpg',1)
    cv.imshow('image',img)
    cv.setMouseCallback('image',click_event)
    cv.waitKey(0)
    cv.destroyAllWindows(0)
