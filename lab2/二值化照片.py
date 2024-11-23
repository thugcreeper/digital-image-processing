import numpy as np
import cv2
#將圖片轉成二值化影像
img=cv2.imread('test.png',cv2.IMREAD_GRAYSCALE)#將照片讀取成灰階圖
meanValue=img.mean()
print(meanValue)
# 讓視窗可以自由縮放大小
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
ret, convert = cv2.threshold(img,meanValue,255,cv2.THRESH_BINARY)#將灰階圖轉換成二值化 大於mean就變成255(白色)
cv2.imshow('image',convert) #'image' is the window's name
cv2.waitKey(0)
cv2.imwrite("newimage.jpg", convert)
cv2.destroyAllWindows()