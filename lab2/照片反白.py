import numpy as np
import cv2
#將圖片反白
img=cv2.imread('test.png',cv2.IMREAD_GRAYSCALE)#sample image將照片讀取成灰階圖
img=255-(np.array(img))
#img = cv2.bitwise_not(img)#use not to invert color
# 讓視窗可以自由縮放大小
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img) #'image' is the window's name
cv2.waitKey(0)
cv2.destroyAllWindows()