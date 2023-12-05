from math import *

choice = input("Choose the operation:\n*, +, -, \n /, **, sqrt, \n %, pythagoras,  rectangle area, \n perimeter of the rectangle , the size , area of ​​triangle , area of ​​a trapezoid:\n ")

if choice == "*":

    num1= float(input("Enter the first number:")) #user input
    
    num2= float(input("Enter the second number:" ))
    
    total= num1*num2
    
    print(f"{num1} * {num2} = {total}")
    
    
elif choice=='-':
    
    num1= float(input("Enter the first number:")) #user input
    
    num2= float(input("Enter the second number:" ))
    
    total= num1-num2
    
    print(f"{num1} - {num2} = {total}")


elif choice=='+':
    
    num1= float(input("Enter the first number:")) #user input
    
    num2= float(input("Enter the second number:" ))
    
    total= num1+num2
    
    print(f"{num1} + {num2} = {total}")
    
    
elif choice=='/':
    
    num1= float(input("Enter the first number:")) #user input
    
    num2= float(input("Enter the second number:" ))
    
    total= num1/num2
    
    print(f"{num1} / {num2} = {total}")
    
    
elif choice =="**":
    
    num1= float(input("Enter the first number:")) #user input
    
    num2= float(input("Enter the second number:" ))
    
    total = num1**num2
    
    print(total)


elif choice=="sqrt":
    
    num1= float(input("Enter any number:")) #user input
    
    num1s= sqrt(num1)
    
    print(num1s)
    

elif choice=="%":
    
    num1=float(input("Enter the first number:")) 
    
    num2=float(input("Enter the second number:")) 
    
    nump= num1 * num2 
    
    total= nump / 100
    
    print(total)


elif choice== 'pythagoras' :
    
    choice2 = input("hypotenuse , leg:")
    
    if choice2 == "hypotenuse":
        
        num1=float(input("Enter the first number:"))
    
        num2=float(input("Enter the second number:"))
        
        tendontotal=num1 ** 2 + num2 **2
        
        total2= tendontotal ** 0.5
    
        print(total2)
    
    if choice2 == "leg":
    
        num1=float(input("Enter the first number:"))
    
        num2=float(input("Enter the second number:"))
        
        legtotal= num1 **2 - num2 **2
        
        total3= legtotal **0.5
        
        print(total3)
        
elif choice == 'rectangle area':
    
    num1=float(input("Enter the first number:"))
    
    num2=float(input("Enter the second number:"))
    
    total1= num1 * num2
    
    print(total1)
    
elif choice == 'perimeter of the rectangle':
    
    num1=float(input("Enter the first number:"))
    
    num2=float(input("Enter the second number:"))
    
    numtotal1 = num1 + num1
    
    numtotal2= num2 + num2
    
    nump = numtotal1 + numtotal2
    
    print(nump)
    
    
elif choice == "the size":
    
    num1=float(input("Enter the first number:"))
    
    num2=float(input("Enter the second number:"))
    
    num3=float(input("choose third number:"))
    
    total = num1 * num2 * num3
    
    print(total)
    
    
elif choice == "area of ​​triangle":
    
    num1 = float(input("choose triangle's base:"))
    
    num2 = float(input("choose triangle height:"))
    
    total = num1 / 2
    
    total1 = total * num2
    
    print(total1)


elif choice == "area of ​​a trapezoid":
    
    num1= float(input("Choose the first base:"))
    
    num2= float(input("Choose the second base:"))
    
    num3= float(input("choose height:"))
    
    total = num1 + num2 / 2
    
    total1 = total * num3
    
    print(total1)
    
    
    

