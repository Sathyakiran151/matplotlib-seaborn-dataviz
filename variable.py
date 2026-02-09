"""1 .Declare variables for your name, age, and height. Print them. """
name = "Sathya"
age = 21
height = 5.5
print( name , age , height)
 

'''2. Find the type of 3.14, "Hello", True, 5.'''
print(type(3.14))
print(type("hello"))
print(type(True))
print(type(5))

'''3 .Convert an integer to float and vice versa.'''
print(float(5)) 
print(int(5.3))



'''4. Take user input for age and print it.'''
Age =int(input("Enter you age :"))
print("MY Age is :" , Age)

'''5.Swap two variables without using a third variable.'''
a= 5
b= 2
a=a+b
b= a-b
a= a-b
print(a,b)

'''
6. Assign multiple values in a single line.'''
a,b,c,d=1,3,5,9
print(a,b,c,d)

'''7 .Check the type of None' '''
print(type(None))


#Take two numbers as input and print their sum.
a=int(input())
b=int(input())
print(a+b)
#Convert a given number of minutes into hours + minutes.
a=int(input("Min"))
hours=a//60
minutes=a%60
print(hours ,"hours and", minutes ,"minutes" )


#Swap two variables without using a third variable.
a=12
b=23
a,b=b,a
print(a,b)

#Take your name and print the first and last character.
a=input()
print(a[0])
print(a[-1])
#Convert temperature from Celsius to Fahrenheit.
C=float(input("Enter the Celsius :"))
F=(C*9/5)+32
print("THE CONERSION OF CELSIUS TO FAHRENHEIT:",F)