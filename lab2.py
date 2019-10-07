# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
#excerse one
name=input("Please enter your name")
number=int(input("Please enter a number that you want it to be repeated"))
if number < 10:
    for i in range(0, number):
        print(name)
else:
    for i in range(0,3):
        print("Too High")

#execises two
total=0
for i in range(0,5):
    num=int(input("enter the number"))
    include=str(input("do you want to include it? yes or no"))
    if include.lower()=="yes":
        total+=num
print("The total is ",total)

#execises three

updown=input("up or down")
if updown.lower()=="up":
    top=int(input("please enter a top number"))
    i=1
    while i<=top:
        print(i)
        i+=1
elif updown.lower()=="down":
    down=int(input("Please enter a number lower than 20"))
    if down<20:
        i=20
        while i>=down:
            print(i)
            i-=1
    else:
        print("lower than 20 please")
else:
    print("I dont understand")


#execise four
total=0
num1=int(input("give me a number"))
num2=int(input("give me another number"))
total=num1+num2
print(total)
addmore=str(input("hey, you want to add more??? enter y or n"))
more=True
while more==True:
    
    if addmore.lower()=="y":
        more=True
        tempnum=int(input("give me a number then"))
        total+=tempnum
        addmore=str(input("hey, you want to add more??? enter y or n"))
    else:
        more=False
print("the total", total)

#execise five
compnum=50
count=1
guess=int(input("make a guess baby"))
while guess!=compnum:
    if guess<compnum:
        print("too low")
    elif guess>compnum:
        print("too high")
    guess=int(input("make a new guess baby"))
    count+=1
print("Well done, you took ", count,"attempts")


#execise six
sixnum=10

while sixnum>0:
    print("There are ",sixnum," green bottles hanging on the wall, ",sixnum," green bottle hanging on the wall, and is 1 green bottle should accidentally fall")
    guess6=int(input("how many green bottles will be hanging on the wall?"))
    while guess6!=sixnum-1:
        print("No, try again")
        guess6=int(input("how many green bottles will be hanging on the wall?"))
    sixnum-=1
    if sixnum==0:
        print("There are no more green bottles hanging on the wall")
    else:
        print("There will be", guess6," green bottles hanging on the wall")

 
#execise seven
def userinput():
    num=int(input("Please enter a number"))
    return num
def countdown(num):
    for i in range(1, num+1):
        print(i)
def main():
    num=userinput()
    countdown(num)
main()

#execise eight
name_list=[]
quit=False
while quit==False:
    commond=str(input("Menu \n 1.ADD. add name to the list\n 2.CHANGE. change the name in the list\n 3.DELETE. delete a name from the list 4.VIEW. view all the names in the list. 5.QUIT quit the program\n"))
    if commond.upper()=="ADD":
        name_list.append(input("Please give me a name"))
        
    elif commond.upper()=="CHANGE":
        changename=str(input("what name do you want to change?"))
        if changename in name_list:
            print("Find the name you want to change, it is at index", name_list.index(changename))
            newname=str(input("So what name do you want to change it to?"))
            name_list[name_list.index(changename)]=newname
        else:
            print("The name is not found")
    elif commond.upper()=="DELETE":
        deletename=str(input("what name do you want to delete"))
        if deletename in name_list:
            print("Find the name you want to delete, it is at index", name_list.index(deletename))
            name_list.remove(deletename)
        else:
            print("The name is not found")
    elif commond.upper()=="VIEW":
        for i in name_list:
            print(i)
    elif commond.upper()=="QUIT":
        quit=True
    else:
        print("Please follow the menu")
    
#execise nine

import random
fruit=random.choice(["apple","banana","peach","strawberry","watermelon"])
print(fruit)
"""
#execise ten
import random
guess=random.choice(["h","t"])
userguess=str(input("guess which? h or t?"))
if userguess==guess:
    print("you win")
elif userguess=="h" or userguess=="t":
    print("bad luck")
else:
    print("wrong input")
print("the pc choose",guess)

#execise eleven
