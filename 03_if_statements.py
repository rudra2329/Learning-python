#Code_01
#using if statement checking eligibility
age=int(input("Enter a number:")) 
if(age>=18):
    print("you are eligible to vote")

#Code_02
#using if and else statement checking odd or even
Num=int(input("Enter a number:")) 
if(Num%3):
    print("odd number") 
else:
    print("even number")

#code_03
#using if,elif,else finding grade 
Mark=int(input("Enter a number:")) 
if(Mark>=90):
    print("A grade") 
elif(Mark>=80):
    print("B grade") 
elif(Mark>=60):
    print("C grade") 
else:
    print("Fail")

#code_04
#To find which is greater
a=int(input("Enter a first number:")) 
b=int(input("Enter a second number:"))
if(a>b):
    print("A is greater") 
elif(a==b): 
    print("Both are equal") 
else:
    print("B is greater")

#Code_05
#To find positive or negative
a=int(input("Enter a number:")) 
if(a>0):
    print("Positive") 
elif(a<0):
    print("Negative") 
else:
    print("Zero")
