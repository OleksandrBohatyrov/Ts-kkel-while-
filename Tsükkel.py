from math import *
from random import *
#0

#a=random.randint(1, 100)

#b=0

#while b != a:
#    try:
#        b = int(input("sisesta arv vahemikus 1-100: ")) 
#        if b>100 or b<1:
#            print("Vahemik on vale")         
#        if b < a:
#            print("Liiga väike! Proovi uuesti.")
#        elif b > a:
#            print("Liiga suur! Proovi uuesti.")
#        else:
#            print("Palju õnne! Sa arvasid mõistatuslik numbri ära.", a)
#    except:
#        print("Value Error")


#----------------------------------------------

#a=random.randint(1, 100)

#b=0

#while True:
#    b = int(input("sisesta arv vahemikus 1-100: ")) 
#    if b>100 or b<1:
#        print("Vahemik on vale")         
#    if b < a:
#        print("Liiga väike! Proovi uuesti.")
#    elif b > a:
#        print("Liiga suur! Proovi uuesti.")
#    else:
#        print("Palju õnne! Sa arvasid mõistatuslik numbri ära.", a)
#        break


#----------------------------------------------
#ulesanne 17
try:
    num_horiz=int(input("Sisesta ruutude arv horisontaalselt =>> \n"))
except:
    print("Value Error")
    num_horiz=randint(1, 20)
try:
    num_vert=int(input("Sisesta ruutude arv vertikalselt =>> \n"))
except:
    print("Value Error")
    num_vert=randint(1, 20)

for y in range(num_vert):
    for x in range(num_horiz):
        print("□", end=" ")
    print()























#-----------------------------------------------
#x=1
#while True:
#    if x>100:
#        break
#    elif x%5==0:
#        print(x, end=" ")
#    x+=1