from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img=Image.open('test.png')
img = img.convert('L')#轉成灰階圖片
OriginalImage=np.asarray(img)#use numpy to read image to 2 dimension matrix
HalfToneImage =np.asarray([[0] * 512 for i in range(512)])#512*512
print(OriginalImage.shape)#shape=512*512
print(type(HalfToneImage))
print(OriginalImage.shape)#shape=512*512
print(OriginalImage)
print(type(HalfToneImage))
print(HalfToneImage.shape)
define_block = [
    [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
    [[1, 1, 1, 1], [1, 1, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
    [[1, 1, 1, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]],
    [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]],
    [[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]],
    [[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]],
    [[1, 1, 1, 1], [1, 0, 0, 0], [0, 0, 0, 1], [1, 1, 1, 1]],
    [[1, 1, 1, 1], [1, 0, 0, 0], [0, 0, 0, 1], [1, 1, 0, 1]],
    [[1, 0, 1, 1], [1, 0, 0, 0], [0, 0, 0, 1], [1, 1, 0, 1]],
    [[0, 0, 0, 0], [0, 1, 1, 1], [1, 1, 1, 0], [0, 0, 1, 0]],
    [[0, 0, 0, 0], [0, 1, 1, 1], [1, 1, 1, 0], [0, 0, 0, 0]],
    [[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 1, 0], [0, 0, 0, 0]],
    [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]],
    [[0, 0, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]],
    [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]],
    [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
]
block_gray=[]
sum=0
for i in range(17):#0-16
  sum=0
  for j in range(4):
    for k in range(4):
      if(define_block[i][j][k]==1):
        sum+=255
  block_gray.append(sum/16)
#print(f"{block_gray}")
minvalue=0.0
minindex=0
for i in range(0,512,4):
  for j in range(0,512,4):
    sum = 0
    minvalue = 0.0
    minindex = 0
    for x in range(4):
      for y in range(4):
        sum += OriginalImage[i+x][j+y]
    sum=sum/16
    for x in range(17):
      if (x==0):
        minvalue = (int)(abs(sum-block_gray[0]))
        minindex = 0;
      else:
        if (minvalue > (int)(abs(sum-block_gray[x]))):
          minvalue = (int)(abs(sum-block_gray[x]))
          minindex = x
    for x in range(4):
      for y in range(4):
        if(define_block[minindex][x][y]==1):
          HalfToneImage[i+x][j+y]=255
        else:
          HalfToneImage[i+x][j+y]=0
#print(HalfToneImage)
data = Image.fromarray(np.uint8(HalfToneImage))
data.show()