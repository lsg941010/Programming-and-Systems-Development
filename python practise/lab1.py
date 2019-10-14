#Exercise One
number =int(input("Please enter the number of loaves you purchased\n"))
regularPrice= number * 3.49
discount= number* 3.49* 60/100
total=regularPrice-discount
print("Regular Price  %5.2f" %(regularPrice),"\nDiscount Price %5.2f" %(discount),"\nTotal Price    %5.2f" %(total))

#Exercise Two
song=str(input("Please enter your favorite song\n"))
print("The length of the string is ",len(song))
startnumber=int(input("Please enter the start number\n"))
endnumber=int(input("Please enter the end number\n"))
if startnumber>=1 and endnumber>=1:
    print("The string is ",song[startnumber-1:endnumber])
else:
    print("wrong number, re-enter\n")

#Exercise Three
firstname=input("Please enter your first name\n")
if len(firstname)<5:
    surname=input("Please enter your surname\n")
    str= firstname+surname
    print(str.upper())
else:
    print(firstname.lower())

#Exercise Four
word=input("Please enter the Pig Latin Word\n")
if(word.isalpha()):
    firstword=word[:1]
    if firstword=='a' or firstword=='e' or firstword=='i' or firstword=='o' or firstword=='u':
        str=word+'way'
        print(str.lower())
    else:
        str=word[1:]+word[:1]+'ay'
        print(str.lower())
else:
    print("Enter a word please")
    

#Exercise Five
answer=input("Is it raining? Enter yes or no\n")
if answer.lower()=="yes":
    answer2=input("Is it windy? Enter yes or no\n")
    if answer2.lower()=="yes":
        print("It's too windy for an umbrella\n")
    else:
        print("Take an umbrella\n")
else:
    print("Enjoy your day\n")

#Exercise Six
age=int(input("How old are you?\n"))
if age>=18:
    print("you can vote")
elif age==17:
    print("You can learn how to drive")
elif age==16:
    print("You can buy a lottery ticket")
else:
    print("you can go Trick-or-Treating")
    
#Exercise Seven
EvenorOdd=int(input("Please enter a number\n"))
if (EvenorOdd%2)==0:
    print("The integer is Even")
else:
    print("The integer is Odd")

#Exercise Eight
letter=input("Please give me a letter\n")
if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
    print("The letter is a vowel")
elif letter=='y':
    print("y is a vowel, sometimes a consonant")
else:
    print("The letter is a consonant")

#Exercise Nine
sides=int(input("Please enter the number of a shape\n"))
if sides==3:
    print("Triangle")
elif sides==4:
    print("Quarliateral")
elif sides==5:
    print("Pentagon")
elif sides==6:
    print("Hexagon")
elif sides==7:
    print("Heptagon")
elif sides==8:
    print("Octagon")
elif sides==9:
    print("Nonagon")
elif sides==10:
    print("Decagon")
else:
    print("Please enter a proper number")
    
#Exercise Ten
one=int(input("Please enter length one\n"))
two=int(input("Please enter length 2\n"))
three=int(input("Please enter length 3\n"))
if one==two and two==three:
    print("Equilateral")
elif one==two or two==three or one==three:
    print("Isosceles")
else:
    print("scalene")
    
#Exercise Eleven
Theanswer=int(input("1)Square\n 2)Triangle\n Enter a number"))
if Theanswer==1:
    lengthofA=int(input("Enter the length of it's sides\n"))
    print(lengthofA*lengthofA)
else:
    Height=int(input("Enter the height of triangle\n"))
    base=int(input("Enter the base of triangle\n"))
    print(Height*base/2)