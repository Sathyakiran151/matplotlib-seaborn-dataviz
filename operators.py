'''2. Operators & Input/Output

🟢 Easy'''

'''1.Add, subtract, multiply, divide two numbers.'''
a= int(input("Enter the numbers :"))
b = int (input("enter the numbers :"))
print("Addition of the two numbers:",a+b)
print("Sunratctipn of the two numbers:",a-b)
print("multipilcation of the two numbers:",a*b)
print(" division of the two numbers:",a/b)


'''2.Use // and % operators.'''
a= int(input("Enter the numbers :"))
b = int (input("enter the numbers :"))
print(" Floor of two numbers :",a//b)
print(" Reminder of two numbers :", a%b)

'''3.Take input and print it.'''
name = ("Enter your name :")
print("My name is :",name)

age = int(input("Enter your age :"))
print("my age is :",age)

'''4.Demonstrate == vs is.'''
a= 10
b=10
print(a==b)
print(a is b)

'''5.Show use of and, or, not.'''
a =int(input("Enter the number :"))
b=int(input(("Enter the number :")))
print(a==b and a>b)
print(a==b or a<b)
print(not(a==b))

'''6.Square a number using **.'''
a=int(input("Enter the number :"))
b=int(input(("Enter the number :")))
print("Sqaure of the two number :",a*b)


'''Concatenate two strings.'''

# Medium

# 8. Write a program to check if a number is even or odd.
a= int(input("Enter the numberes :"))
if a%2 ==0:
    print("Number is even")
else:
    print("number is odd")
    
# 9. Write a program to find remainder without using %.
num = int(input("Enter the numbers :"))
divided= int(input("Enter the numbers :"))
quetient = num//divided
reminder = num -(quetient*divided)
print("Remainder is :",reminder)

# 12. Take two inputs and compare them.
a =int(input("Enter the number :"))
b=int(input(("Enter the number :")))
print(" is both values are equal :",a==b )
print(" is both values are not eqaul :",a!=b)
      
#13. Use +=, -=, *=, /= operators.

a =int(input("Enter the number :"))
b=int(input(("Enter the number :")))
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)







#14. Input radius and calculate circle area.