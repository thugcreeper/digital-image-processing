import numpy as np
import cv2

img=cv2.imread('pic1.jpg',cv2.IMREAD_COLOR)
print("width: {} pixels".format(img.shape[1]))
print("height: {} pixels".format(img.shape[0]))
print("channels: {}".format(img.shape[2]))
# 讓視窗可以自由縮放大小
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

cv2.imshow('image',img) #'image' is the window's name
cv2.waitKey(0)
cv2.imwrite("newimage.jpg", img)
cv2.destroyAllWindows()