'''for i,j in {1:'abc',22:'kiran','pythonlife':1}.items():
    print(i,j)'''

#🟢 Easy (Basics)

#Create a dictionary of your name, age, and city.
a ={'name':"sathya","age":19,"city":'hyderabad'}
print(a)

#Access and print the value of a specific key.
a ={'name':"sathya","age":19,"city":'hyderabad'}
print(a.get('name'))

#Add a new key–value pair to the dictionary.
a ={'name':"sathya","age":19,"city":'hyderabad'}
a.update({'kiran':232})
print(a)
#Update an existing key’s value.
a ={'name':"sathya","age":19,"city":'hyderabad'}
a.update({'name':2})
print(a)

#Remove a key using pop().
a ={'name':"sathya","age":19,"city":'hyderabad'}
print(a.pop("age"))

#Find the number of items in a dictionary using len().
a ={'name':"sathya","age":19,"city":'hyderabad'}
print(len(a))

#Print all keys using keys() method.
a ={'name':"sathya","age":19,"city":'hyderabad'}
print(a.keys())


#🟡 Medium (Operations)

#Print all values using values().
a ={'name':"sathya","age":19,"city":'hyderabad'}
print(a.values())



#Print all key–value pairs using a for loop.
for i,j in {'kiram':12,"satya":13,"aditya":16,"sai":17,'rohan':10}.items():
    print(i,j)


#Create a dictionary of 5 students with their marks. Print only the names.
b={'kiram':12,"satya":13,"aditya":16,"sai":17,'rohan':10}
print(b.keys())


#Check if a key exists in the dictionary using in.
b={'kiram':"sat","ate":1,"cat":'hybrid'}
if 'kiram' in b:
    print("exists")

#Merge two dictionaries using update().
a ={'name':"sathya","age":19,"city":'hyderabad'}
a.update(b={'kiram':"sat","ate":1,"cat":'hybrid'})
print(a)


#Copy a dictionary and modify one of them.

#Use get() method to safely access a key that may not exist.

