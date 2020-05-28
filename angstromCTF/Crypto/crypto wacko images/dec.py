from numpy import *
from PIL import Image

flag = Image.open(r"flag.png")
img = array(flag)

key = [41, 37, 23]
tab41 = []
tab37 = []
tab23 = []
    
a, b, c = img.shape

for j in range (0, 256):
    tab41.append(j * 41 % 251)
    tab37.append(j * 37 % 251)
    tab23.append(j * 23 % 251)

for x in range (0, a):
    for y in range (0, b):
        pixel = img[x, y]
        for i in range(0,3):
            if  i == 0:
                pixel[i] = tab41.index(pixel[i])
            else if  i == 1:
                pixel[i] = tab37.index(pixel[i])
            else if  i == 2:
                pixel[i] = tab23.index(pixel[i])
        img[x][y] = pixel

enc = Image.fromarray(img)
enc.save('enc.png')