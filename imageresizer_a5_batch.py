from PIL import Image
import os, sys

path= (os.getcwd()+"/pics/")

isExist = os.path.exists(path+".DS_Store")
print(isExist)

if isExist == True:
    os.remove(path + ".DS_Store")
else:
    pass

#create lists to store data 
imageopenlist=[]
filenamelist=[]
ratiolist=[]
llist=[]
hlist=[]


#loop over pictures to store its data in lists
for i in os.listdir(path):
    im = Image.open(path + i)
    ratioofimage = (im.size[0] / im.size[1])
    l = im.size[0]
    h = im.size[1]
    imageopenlist.append(im)
    filenamelist.append(i)
    ratiolist.append(ratioofimage)
    llist.append(l)
    hlist.append(h)
    
#define page size and convert it from mm to point
lSizeinmm= 210
hSizeinmm= 148
lSizeinpt =  (lSizeinmm / 0.352778)
hSizeinpt =  (hSizeinmm / 0.352778)

#create 2 lists for setting the right ratio 
newLlist=[]
newHlist=[]

#loop over pictures to write the right ratio into the lists
for i in range(len(llist)):
    im = imageopenlist[i]
    if ratiolist[i] > 1:
        newL = round (lSizeinpt)
        newH = round (lSizeinpt / ratiolist[i])
    elif ratiolist[i] == 1:
        newL = round (hSizeinpt)
        newH = round (hSizeinpt)
    else:
        newL = round (lSizeinpt * ratiolist[i])
        newH = round (lSizeinpt)
        
    newLlist.append(newL)
    newHlist.append(newH)
    
    print(round(newLlist[i]*0.352778), round(newHlist[i]*0.352778), round (ratiolist[i], 2))
    
    
    #resized_im = im.resize((newLlist[i],newHlist[i]))
    #resized_im.save(path + "_______" + filenamelist[i])