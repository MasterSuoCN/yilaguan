###20171214
###易拉罐瓶身转换

import time
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math

def PictureChange(filename,Left_x=None,Right_x=None):
    Img = Image.open(filename)
    width,height = Img.size
    Mid_Pos = (Right_x-Left_x)/2+Left_x
    Target_Width = Right_x-Left_x
    fill_data = np.zeros(width+500)
    
    
    Img_data=np.array(Img.getdata()).reshape(height,width,3)
    New_Img_data=np.ones((height,width+500,3))

    for w in range(Left_x,Right_x+1):
        ##格式转换函数
        x=(math.pi/2-math.acos((w-Mid_Pos)*2/Target_Width))*(Target_Width/2)
        New_Img_data[:,round(x+Mid_Pos),:]=Img_data[:,w,:]

        fill_data[round(x+Mid_Pos)] = w-Left_x
        if(w==Right_x):
            fill_data[round(x+Mid_Pos)] = 432.1   #标记结尾

    #去黑边(边缘部分待优化)
    for i in range(width+499):
        #print("<><><>")
        if fill_data[i]!= 0.0:
            if fill_data[i] == 432.1:
                break
            if fill_data[i+1]== 0.0:
                New_Img_data[:,i+1,:] = New_Img_data[:,i,:]
        else:
            continue
    #反向去黑边(有改善)
    j = width+500
    while j>0:
        j = j-1
        if fill_data[j]!= 0.0:
            if fill_data[j-1]== 0.0:
                New_Img_data[:,j-1,:] = New_Img_data[:,j,:]
        else:
            continue

    return New_Img_data

filename = "50.bmp"

plt.figure("123")

start = time.time()
plt.imshow(PictureChange(filename,827,1277)/255.0)
plt.grid(False)
plt.savefig('result111.png', dpi = 500)
print (time.time()-start)

plt.show()

