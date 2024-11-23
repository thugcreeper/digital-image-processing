import cv2
import numpy as np

img = cv2.imread('test.png')
img = np.array(img)
print(img)
img=img//64
img*=64
print("-------------------")
print(img)
cv2.imshow('img/64')
cv2.waitKey(0)
cv2.destroyAllWindows()