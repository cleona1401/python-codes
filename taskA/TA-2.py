def adi():                      #add function will take two nos from user and add them and store them in variable add
    a=int(input("enter 1st no:")) 
    b=int(input("enter 2nd no:"))
    add=a+b
    print("sum is :",add)
def sub():                      #subtract function will take two nos from user and subtract them and store them in variable subt
    a=int(input("enter 1st no:"))
    b=int(input("enter 2nd no:"))
    subt=a-b
    print("sub is :",subt)
def mul():                      #multiply function will take two nos from user and multiply them and store them in variable mul
    a=int(input("enter 1st no:"))
    b=int(input("enter 2nd no:"))
    mult=a*b
    print("multiplication is :",mult)
def div():                      #division function will take two nos from user and divide them and store them in variable divi
    a=int(input("enter 1st no:"))
    b=int(input("enter 2nd no:"))
    divi=a/b
    print("division is :",divi)
def spe():                      #speed function will take distance and time from user divide dist by time and store in speed variable
    dist=float(input("enter distance :"))
    time=float(input("Enter time:"))
    speed=dist/time
    print("speed is:",speed)
def distance():                 #distance function will take coordinates of two points from user and susstitute them in formula and store them in variable result
    x1=float(input("enter x1: "))
    x2=float(input("enter x2: "))
    y1=float(input("enter y1: "))
    y2=float(input("enter y2: "))
    result= ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)
    print("distance is:",result)
def interest():                 #interest function will take pricipal amt,rate of interest and time period from user put it in formula and store  in variable si.
    princi=int(input("enter principal:"))
    rate=int(input("enter rate of interest:"))
    tp=int(input("enter time period:"))
    si=(princi*rate*tp)/100
    print("simple interest is:",si)
while True:             #will alow you to enter your choice till user press exit(i.e cho==8)
    cho=int(input("enter your choice:\n 1:sum\n 2:sub\n 3:mul\n 4:div\n 5:distance\n 6:speed\n 7:interest\n 8:exit"))#will ask user about the operation he wants to perform
    if cho==1:
        adi()   #call function addition function
    elif cho==2:
        sub()   #call function subtract function
    elif cho==3:
        mul()   #call multiplication function
    elif cho==4:
        div()   #call division function
    elif cho==5:
        distance() #call distance function
    elif cho==6:
        spe()   #call speed function
    elif cho==7:
        interest()#call interest function
    elif cho==8:
        exit()  #if user wants to exit
    else:
        print("invalid choice")#if user enter any other wrong choice then it will print invalid choice
        
""""op:C:\Users\91839\Desktop\pycourse>python spd.py
enter your choice:
 1:sum
 2:sub
 3:mul
 4:div
 5:distance
 6:speed
 7:interest
 8:exit1
enter 1st no:8
enter 2nd no:2
sum is : 10
enter your choice:
 1:sum
 2:sub
 3:mul
 4:div
 5:distance
 6:speed
 7:interest
 8:exit2
enter 1st no:7
enter 2nd no:3
sub is : 4
enter your choice:
 1:sum
 2:sub
 3:mul
 4:div
 5:distance
 6:speed
 7:interest
 8:exit3
enter 1st no:8
enter 2nd no:3
multiplication is : 24
enter your choice:
 1:sum
 2:sub
 3:mul
 4:div
 5:distance
 6:speed
 7:interest
 8:exit4
enter 1st no:23
enter 2nd no:8
division is : 2.875
enter your choice:
 1:sum
 2:sub
 3:mul
 4:div
 5:distance
 6:speed
 7:interest
 8:exit5
enter x1: 4
enter x2: 6
enter y1: 2
enter y2: 6
distance is: 4.47213595499958
enter your choice:
 1:sum
 2:sub
 3:mul
 4:div
 5:distance
 6:speed
 7:interest
 8:exit6
enter distance :50
Enter time:2
speed is: 25.0
enter your choice:
 1:sum
 2:sub
 3:mul
 4:div
 5:distance
 6:speed
 7:interest
 8:exit7
enter principal:1000
enter rate of interest:1
enter time period:2
simple interest is: 20.0
enter your choice:
 1:sum
 2:sub
 3:mul
 4:div
 5:distance
 6:speed
 7:interest
 8:exit8

C:\Users\91839\Desktop\pycourse>"""

        