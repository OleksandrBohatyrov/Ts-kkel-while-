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
#try:
#    num_horiz=int(input("Sisesta ruutude arv horisontaalselt =>> \n"))
#except:
#    print("Value Error")
#    num_horiz=randint(1, 20)
#try:
#    num_vert=int(input("Sisesta ruutude arv vertikalselt =>> \n"))
#except:
#    print("Value Error")
#    num_vert=randint(1, 20)

#for y in range(num_vert):
#    for x in range(num_horiz):
#        print("□", end=" ")
#    print()


#-----------------------------------------------
#x=1
#while True:
#    if x>100:
#        break
#    elif x%5==0:
#        print(x, end=" ")
#    x+=1


#ans=randint(1,10)
#while True:
#    g=input("mis numbri ma arvasin?(1-10, mängu lõpetamiseks kirjutage *lõpp* ) \n")
#    if g.lower()=="lopp":
#        print("mäng on läbi!")
#        break
#    if not g.isnumeric():
#        print("Vale andmetüpp!")
#        continue
#    g=int(g)
#    if g ==ans:
#        print("õige! sa arvasid ära!") 
#        break
#    if g>10 or g<1:
#        print("Vahemik on vale!")
#    elif g != ans:
#        print("vale! proovi veel korra!")
#        continue


#Ülesanne 3
#g=1
#try:
#    f=int(input("mitu ülesandeid sa tahad? "))
#    for d in range (0,f,1):
#        print(f"Ülesanneü {g}: ")
#        a = randint(1,50)
#        b = randint(1,50)
#        c=a+b
#        for i in range(0,5,1):
#            answer=int(input(f"{a}+{b}=?"))
#            if answer == a+b:
#                print("see on õige")
#                break
#            else:
#                print("Proovi veel korra")
#                print()
#        g=g+1
#        print(f"õige on {c} ")
#except:
#    print("see ei ole õige")


##ulesanne 13
#print("arv", "  ruut", "  kuup")
#for i in range(1, 11):
#    print(f" {i}      {i**2}        {i**3}")
#print("teine variant")
##ulesanne 13-2
#print("arv", "  ruut", "  kuup")
#i = 1
#while i<11:
#     print(f" {i}      {i**2}        {i**3}")
#     i += 1

#import string
#print("Arva taht - (from Aa to Zz)")
#letter = random.choice(string.ascii_letters)

#while True:
#    answ = str(input("Teie oletus: "))
#    if letter == answ:
#        print("Tubli!")
#        break
#    else: print("Provi uuesti!")


#ulesanne 6
#print()
#print("Ulesanne 6 1")
#print()
#for i in range(0,5):
#    print("* "*5)
#print()
#for i in range(0,10):
#    print("* "*i)
#print()
#for i in range(0,10):
#    print("* "*(10-i))
#print()

#ulesanne 8

#while True:
#    try:
#        mainnumber = int(input("Vali number 1-100: "))
#        break
#    except: print("See pole täisarv")
#if mainnumber<1 or mainnumber>100:
#    print("vali õige number")
#else:
#    paaris = 0
#    paaritu = 0
#    x = 0
#    while x != mainnumber:
#        x = x + 1
#        print(int(x), end =" ")
#        if x % 2 == 0:
#            paaris += 1
#        else:
#            paaritu += 1

#print("Paaris numbrid", paaris)
#print("Paaritu numbrid", paaritu)

#ulesanne 11

n=randint(1,10)
while True:
    text = input("Väljumiseks sisetage number: ")
    if text == "stopp":
        print("Välju programmist! Kohtumiseni! See sai tehtud", n)
        break
    elif int(text) == n:
        print("palju õnne, sa võitsid")
        break
    else:
        print("proovi veel korra")
    if a == 3:
        print("3 katset ammendatud")
        break
