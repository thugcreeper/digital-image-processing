from PIL import Image,ImageOps
import matplotlib.pyplot as plt
import numpy as np
img=Image.open('900pxkou.png')
img =np.array(img)
w,h,channel=img.shape
print(w,h,channel)
n=4
for i in range(0,w,n):#try to get pixel style?
  for j in range(0,h,n):
    sum = np.zeros(channel)#rgb image has 3 channel
    for x in range(n):#get average of 16 pixel
      for y in range(n):
        if(i+x<w and j+y<h):
          sum+=img[i+x][j+y]
    sum/=n*n
    for x in range(n):
      for y in range(n):
        if(i+x<w and j+y<h):
          img[i+x][j+y]=sum
data = Image.fromarray(np.uint8(img))
plt.imshow(data)
data=data.save('pixel.png')
plt.axis('off')
plt.show()
data.save('pixel.png')