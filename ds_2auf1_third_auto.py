import os


'''
def pnum():
    x = int(input('Give a number: '))
    return x

lastp = pnum()
'''


path= (os.getcwd()+ "/num/")
countpics=[]
for i in os.listdir(path):
    countpics.append(i)

firstp=1
lastp = len(countpics)


pcount=[*range(firstp,lastp+1)]
full= len(pcount)
half = round(len(pcount)/2+1)


list1=[*range(1,half)]
list2=[*range(half,full+1)]
list3=[]

for i in range(0,len(list1),2):
    list3.append(list1[i])
    list3.append(list2[i])
    list3.append(list2[i]+1)
    list3.append(list1[i]+1)
    

list3new = []
duplist = []

for i in list3:
    if i not in list3new:
        list3new.append(i)
    else:
        duplist.append(i)
        

if list3new[-1] > list2[-1]:
    del list3new[-1]
    
def getres():
    return list3new
    
print(list3new)
