import third_auto
from PIL import Image
import os, sys

path= (os.getcwd()+ "/num/")

isExist = os.path.exists(path+".DS_Store")
#print(isExist)

if isExist == True:
    os.remove(path + ".DS_Store")
else:
    pass
    
ds= third_auto.getres()

oldimagename=[]

for i in os.listdir(path):
    oldimagename.append(i)
    
 
oldname=[]
newname=[]
for i in ds:
    oldname.append((oldimagename[i-1]))
    
ran= len(ds) +1
number=[*range(1,ran)]
numberStr = list(map(str, number))


for i in range(len(ds)):
    newname.append(numberStr[i]+".jpg")
    
pathStr= str(path)

'''
for i in range(len(oldname)):
    os.rename(pathStr + oldname[i], pathStr + newname[i])
'''
for i in range(len(oldname)):
    print(pathStr + oldname[i], pathStr + newname[i])

