#Create a list of 5 fruits and print the entire list.
a=["banana","apple","mango","grapes","orange"]
print(type(a))
print(a)


#Access and print the first and last elements of a list.
a=["banana","apple","mango","grapes","orange"]
print("the first element of list a",a[0])
print("the second element of list a",a[-1])

#Write a program to find the length of a list using len().
a=["banana","apple","mango","grapes","orange"]
print(len(a))

#Write a program to add an element "mango" to an existing fruit list using append().
a=["banana","apple","mango","grapes","orange"]
a.append("mango")
print(a)

#Write a program to insert "apple" at the second position in a list.

a=["banana","apple","mango","grapes","orange"]
a.insert(2,"apple")
print(a)


#Write a function sum_list(numbers) that returns the sum of all elements in a list.
def add(list):
    a=[232,1231,1,213]
    sumof_a=sum(a)
    return sumof_a
print(add(list))
  
a=[10,212,12]
res=0
for i in a:
    res+=i
    print(res)

#Write a program to remove an element from a list using remove() or pop().
a=[232,1231,1,213]
a.remove(213)
print(a)
a.pop(1)
print(a)

#Write a function find_max_min(lst) that prints the maximum and minimum elements in a list.
def find_max_min(lst):
    print(max(lst))
    print(min(lst))
find_max_min([23,23,24542,121,121,])
    
#Write a program to sort a list of numbers in ascending order using sort().
a= [23,23,24542,121,121,21]
a.sort(reverse=True)
print(a)
#Write a function count_occurrences(lst, item) that counts how many times a given item appears in'''

#Reverse a list using slicing.
a=["apple","sathya","kiran"]
a.reverse()
print(a)

a=["apple","sathya","kiran"]
print(a[::-1])

#Concatenate two lists into one.
a=["apple","sathya","kiran"]
b=["srinath","athya","sindu"]
concat=a+b
print(concat)
#Find how many times 10 appears in a list.
a=[1,2,235,5,62,10,10,10,10,10,10,10,10,10,1]
print(a.count(10))

