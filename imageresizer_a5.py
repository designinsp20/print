from PIL import Image
import os, sys


path= (r"path2picFolder")
os.remove(path + ".DS_Store")

for n in os.listdir(path):
    im = Image.open(path + n)
    print(im)
    
'''

ratioofimage = (im.size[0] / im.size[1])
lSizeinmm= 210
hSizeinmm= 148
lSizeinpx =  (lSizeinmm / 0.264583333)
hSizeinpx =  (hSizeinmm / 0.264583333)

if ratioofimage < 1:
    newL = round (lSizeinpx * ratioofimage)
    newH = round (lSizeinpx)
else:
    newL = round (lSizeinpx)
    newH = round (lSizeinpx / ratioofimage)

newLinmm = round (newL * 0.264583333)
newHinmm = round (newH * 0.264583333)
print (ratioofimage)
print (newLinmm, newHinmm)

resized_im = im.resize((newL,newH))
resized_im.save(r"path2newpic.jpg")

'''
