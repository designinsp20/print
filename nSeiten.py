#define the lengh and height of the elements
seiteH= 210
seiteL= 297

x = int (input("Please input the height: "))
y = int (input("Please input the lengh: "))

#divide big by small
hx =  seiteH/x
ly =  seiteL/y
hy =  seiteH/y
lx =  seiteL/x
#multiply the lengh and height of opposites (2 options)
zahl1 = (hx*ly)
zahl2 = (hy*lx)
#round down the result (remove the decimals)
zahlrund1 = (int (hx) * int (ly))
zahlrund2 = (int (hy) * int (lx))

#set the final result to the bigger result
if zahlrund1 < zahlrund2:
  st = zahlrund2
else:
  st = zahlrund1

print (st)