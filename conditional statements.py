# Check if number > 10.
number =int(input("Enter the numbers :"))
if number>10:
    print(number , " is greater than 10 ")
elif number <10:
    print(number, "is less than 10 ")

# Print if a number is positive, negative, or zero.
number = int(input("Enter the numbers :"))
if number>0:
    print("Number is postive")
elif number<0:
    print ("Number is negative")
elif number ==0:
    print("Number is equal to zero ")

# Check if age > 18 (eligible to vote).
age = int(input("Enter the age of the person :"))
if age>18:
    print("person is eligible to vote")
else:
    print("Person is not elgible to vote")

# Find the greatest of 2 numbers.
number1 =int(input("Enter the  first number :"))
number2 =int(input("Enter the second number :"))
if number1>number2 :
    print("number1 is greater than number2")
elif number2>number1:
    print("number2  is greater than number1")

# Check if a number is divisible by 5.
num=int(input("Enter the  first number :"))
if num%5==0:
    print("divisible by 5")
else:
    print("not divisible by 5")

# Check if string is empty or not. 
''''

print grade based on marks (if/else).


8. Find largest among 3 numbers.'''
a = int(input("Enter the number :"))
b = int(input("Enter the numbers :"))
c = int(input("Enter the numbers : "))
if a>b and a>c:
    print(a,"is the largest number")
elif b>a and b>c:
    print(b, "is the largest number")
elif c>a and c>b:
    print(c,"is the largest number")




#. Write program to check leap year.
# 10. Nested if example: classify person as child/teen/adult/senior.
age = int(input("Enter your age : "))
if age>0 and age<=12:
    print(" the child age is ", age)
elif age>12 and age<=17:
    print(" the teen age is ", age)
if age>18 and age<=45:
    print(" adult age is ", age)
if age>46 and age<=100:
    print(" senior age is ", age)



# 11. Check if number is within a range.
num = int (input("enter the numbers : "))
if num>=1 and num<=900:
    print(" the number is range of 1 to 900")
elif num<0 or num>900:
    print("the number is out of range ")

'''12. Use elif for grading system.
13. Write a mini ATM: check balance before withdrawal.'''