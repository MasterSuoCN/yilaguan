###20171214
###易拉罐瓶身图像转换

import time
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math

def PictureChange(filename,Left_x=None,Right_x=None):
    Img = Image.open(filename)
    Img_Small=Img.crop((Left_x,0,Right_x,Img.size[1]))
    #Img_Small.show()
    #Img_Small.save(filename+"_small.bmp")
    
    width,height = Img_Small.size
    Left_x=0
    Right_x=width-1
    
    Mid_Pos = (Right_x+Left_x)/2
    Target_Width = Right_x-Left_x
    
    fill_data = np.zeros(width*2)
    
    Img_data=np.array(Img_Small.getdata()).reshape(height,width,3)
    New_Img_data=np.ones((height,width*2,3))

    for w in range(Left_x,Right_x+1):
        ##格式转换函数
        x=(math.pi/2-math.acos((w-Mid_Pos)*2/Target_Width))*(Target_Width/2)
        New_Img_data[:,round(x+width),:]=Img_data[:,w,:]        

        fill_data[round(x+width)] = w-Left_x

        if(w==Right_x):
            fill_data[round(x+width)] = 432.1    #标记结尾

        ##去黑边
    for i in range(width*2):
        if fill_data[i]!= 0.0:
            if fill_data[i] == 432.1:
                break
            if fill_data[i+1]== 0.0:
                New_Img_data[:,i+1,:] = New_Img_data[:,i,:]
                if fill_data[i+1] == 0.0:
                    fill_data[i+1] = fill_data[i]
        else:
            continue

##    k = 699
##    while 699<=k<=1405:
##        print(k,fill_data[k],New_Img_data[400,k,:])
##        k=k+1

    return New_Img_data

filename = "50.bmp"

plt.figure("123")

start = time.time()
plt.imshow(PictureChange(filename,827,1277)/255.0)

print (time.time()-start)

plt.grid(False)
plt.savefig(filename[0:3]+"_result.png", dpi = 500)

plt.show()

