import PIL
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import PIL.ImageOps

img = Image.open("pic1.jpg")
grayImg = img.convert('L')#轉成灰階圖片
#grayImg.save('newimg.png')
invert = PIL.ImageOps.invert(grayImg)

invert.show()#photo name.show()
