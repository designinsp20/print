import os
#1,2,3,4,5,6,7,8,9,10,11,12
#12,1,2,11,10,3,4,9,8,5,6,7
import shutil

path= (os.getcwd()+ "/num/")
path2= (os.getcwd()+"/")

isExist = os.path.exists(path+".DS_Store")
#print(isExist)

if isExist == True:
    os.remove(path + ".DS_Store")
else:
    pass

pics=[]
for i in os.listdir(path):
    pics.append(i)


list1=[*range(1,len(pics)+1)]
list2=[]
list3=[]
listofpower4=[]
ran=len(list1)

for i in range(1,10):
    listofpower4.append(i*4)


if ran in listofpower4:
    val= True
else:
    val= False

rani=round(ran/4)
for i in range(rani):
    
    
    if i == 0 and val== True:
        list2.append(list1[-1])
    elif i == 0 and val== False:
        list2.append(0)
    elif list2[-1] == 0:
        list2.append(list1[-1])
    else:
        list2.append(list2[-1]-1)
        
        
    list2.append(list1[i+i])
    list2.append(list1[i+i+1])
    
    
    if i == 0 and val== True:
        list2.append(list1[-2])
    elif i != 0:
        list2.append(list2[-3]-1)
    else:
        list2.append(0)
        
list1Str = list(map(str, list1))
list2Str = list(map(str, list2))


j=0


for i in list2:
    #os.rename(path + pics[i], path + list1Str[j]+".jpg")
    if i == 0:
        #shutil.copyfile(path2+"x.jpg", path+str(j+1)+".jpg")
        print(path2+"x.jpg", path+str(j+1)+".jpg")
        print()

    else:
        #os.rename(path + pics[i-1], path + list1Str[j] + ".jpg")
        print(path + pics[i-1], path + list1Str[j] + ".jpg")
        print()
    
    j=j+1

