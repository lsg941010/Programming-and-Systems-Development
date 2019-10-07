# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 15:09:44 2019

@author: 2443170L
"""

#Exercises1
"""
again=True
while again==True:
    selection=int(input("1) Create a new file \n 2) Display the file \n 3) Add a new item to the file \n "))
    if selection==1: 
        outf=open("Subjects.txt","w")
        subject=str(input("Please enter a school subject"))
        outf.write(subject)
        outf.close()
    elif selection==2:
        check=open("Subjects.txt","r")
        content=check.read()
        print(content)
        check.close()
    elif selection==3:
        outf=open("Subjects.txt","w")
        subject=str(input("Please enter a school subject"))
        outf.write(subject)
        outf.close()
        outf=open("Subjects.txt","r")
        content=outf.read()
        print(content)
        outf.close()
        
    else:
        again=False
        print("Wrong input")
        
    
#Exercise2 Math Quiz
import random
import csv
name=str(input("what is your name"))
Question_list=["1+1=?","2+3=?","5-3=?"]
question1=random.choice(Question_list)
answer1=str(input(question1))
Question_list.remove(question1)
question2=random.choice(Question_list)
answer2=str(input(question2))
file=open("Mathquiz.csv","a")
newRecord=name+","+question1+","+question2+"\n"+","+answer1+","+answer2+"\n"
file.write(str(newRecord))
file.close()


#Exercise3
import csv 
def addtofile():
    file=open("Salaries.csv","a")
    name=str(input("What's your name pal"))
    salary=str(input("How much is your Salary pal"))
    file.write(name+","+salary+"\n")
    file.close()
    
def display():
    file=open("Salaries.csv","r")
    for row in file:
        print(row+"\n")
    file.close()
    

again=True
while again==True:
    selection=int(input("1) Add to file \n2)View all Records\n3)Quit programme"))
    if selection==1:
        addtofile()
    elif selection==2:
        display()
    elif selection==3:
        again=False
    else:
        print("Please enter a valid number")



#Exercise4
import csv 
def addtofile():
    file=open("Salaries.csv","a")
    name=str(input("What's your name pal"))
    salary=str(input("How much is your Salary pal"))
    file.write(name+","+salary+"\n")
    file.close()
    
def display():
    file=open("Salaries.csv","r")
    for row in file:
        print(row+"\n")
    file.close()
    
def deletrecord():
    file=list(csv.reader(open("Salaries.csv")))
    tmp=[]
    name=str(input("What is the name you want to delete?"))
    for row in file:
        if name in str(row):
            print("The name you want is deleted")
        else:
            tmp.append(row)
        
    #tmp.remove(name)
    file=open("Salaries.csv","w")
    x=0
    for row in tmp:
        newOne=tmp[x][0]+","+tmp[x][1]+"\n"
        file.write(newOne)
        x=x+1
    file.close()
            
again=True
while again==True:
    selection=int(input("1) Add to file \n2)View all Records\n3)Delete a record\n4)Quit programme"))
    if selection==1:
        addtofile()
    elif selection==2:
        display()
    elif selection==3:
        deletrecord()
    elif selection==4:
        again=False
    else:
        print("Please enter a valid number")
        
        
"""
#
        