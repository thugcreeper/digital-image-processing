import numpy as np
from skimage import io
import matplotlib.pyplot as plt
import numpy.matlib
#讀取圖像
img = io.imread('cameraman.tif')
io.imshow(img)
io.show()
# 定義混色矩陣D
D = np.array([[0, 128], [192, 64]])
# 使用repmat來擴展矩陣
r = np.matlib.repmat(D, img.shape[0] // 2, img.shape[1] // 2)
print(r)
# 將圖像與混色矩陣進行比較
x2 = img > r
# 顯示結果
io.imshow(x2)
io.show()
