from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import time

start_time=time.process_time()  #start timming
def get_mosic(img,blocksize):
  w,h,channel=img.shape
  mosaic=np.zeros_like(img)
  for i in range(channel):
    for j in range(0,w,blocksize):
      for k in range(0,h,blocksize):
        block=img[j:min(j+blocksize,w),k:min(k+blocksize,h),i]#min用來避免邊界問題
        mean=np.mean(block)
        mosaic[j:j+blocksize,k:k+blocksize,i]=mean
  return mosaic
lena=io.imread('lena.png')
img=io.imread('test.jpg')#較大的影像
#mosaic=img wrong copy
mosaic1=get_mosic(img,10)
mosaic2=get_mosic(img,50)
lena_m1=get_mosic(lena,10)
lena_m2=get_mosic(lena,50)

titles = ['original', 'block:10*10', 'block:50*50']
images = [[img, mosaic1, mosaic2],
          [lena, lena_m1, lena_m2]]
fig = plt.figure(figsize=(12, 8))
for i in range(2):
 for j in range(3):
    ax = fig.add_subplot(2, 3, i*3 + j + 1)
    ax.set_title(titles[j])
    ax.imshow(images[i][j])

plt.show()
end_time=time.process_time()# end timing
print(f"execution time: {end_time - start_time:.6f} 秒")