#Create a tuple of 5 fruits and print it.
a=("banana","apple","mango","grapes","orange")
print(a)

#Access the second and fourth element of a tuple.
a=("banana","apple","mango","grapes","orange")
print(a[2])
print(a[4])
##Find the length of a tuple.
a=("banana","apple","mango","grapes","orange")
print(len(a))

##Check if "banana" is present in a tuple.
a=("banana","apple","mango","grapes","orange")
print("the banana there in list: ","banana" in a)
#Convert a tuple into a list.

a=("banana","apple","mango","grapes","orange")
print(list(a))

#Repeat a tuple 3 times using * operator.

a=("banana","apple","mango","grapes","orange")
print(a*3)

#Concatenate two tuples and print the result.
a=("banana","apple","mango","grapes","orange")
b=("kiwi","pineapple")
print(a+b)

#find the index of a specific element in a tuple.

a=("banana","apple","mango","grapes","orange")
print(a.index("apple"))

#Count how many times "apple" appears in a tuple.

a=("banana","apple","apple","apple","mango","grapes","orange")
print(a.count("apple"))


#Slice a tuple to print only middle elements.
a=("banana","apple","mango","grapes","orange")
print(a[:])

#Unpack a tuple into individual variables.
detail =("sathya",18,"country")
name,age,identity = detail
print(name)
print(age)
print(identity)
#Convert a list into a tuple using tuple().
a=["banana","apple","mango","grapes","orange"]
print(tuple(a))

#Check if two tuples are equal.
a=["banana","apple","mango","grapes","orange"]
b=["banana","apple","mango","grapes","orange"]
print("the two value of a and b  are equal :",a is b)

#Create a nested tuple and access elements from it.
