import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image,ImageOps

def global_equalize(img):
  final=np.zeros_like(img)
  pixelcount=np.zeros(256,dtype=np.uint)
  total_gray=0
  for pixel in img.ravel():   #ravel轉換成1D array
    pixelcount[pixel]+=1     #count correspond pixel's amount
  cdf=np.cumsum(pixelcount)     #Return the cumulative sum 
  #print(cdf)
  min_cdf=min(cdf)
  total_pixel=img.size       #equal to width*size
  for i in range(len(cdf)):
    final[img==i] = round((cdf[i]-min_cdf)/(total_pixel-min_cdf) * 255)
  final=final.reshape(img.shape)#change from 1D array to 2D array
  return final

def get_cdf(img):
  pixelcount=np.zeros(256,dtype=np.uint)
  for pixel in img.ravel():
    pixelcount[pixel]+=1
  cdf=np.cumsum(pixelcount)
  cdf=cdf/cdf[-1]#divide last element(sum of all grayscale) to make probality between 0-1
  return cdf
img=Image.open('hw4-1.jpg').convert('L')
img=np.array(img)
equalized_img=global_equalize(img)
fig, axes = plt.subplots(3, 2, figsize=(8,8))
axes[0,0].imshow(img,cmap='gray')
axes[0,0].set_title('original')

axes[0,1].imshow(equalized_img,cmap='gray')
axes[0,1].set_title('equalized')

axes[1,0].hist(img.ravel(),bins=256)#show histogram,remember to use.ravel()
axes[1,1].hist(equalized_img.ravel(),bins=256)
cdf=get_cdf(img)
cdf_eq=get_cdf(equalized_img)
axes[2,0].plot(cdf,color='#029386')
axes[2,1].plot(cdf_eq,color='#029386')
plt.show()