# Create a set of 5 numbers and print it.
a={12,213,32,21,2}
print(a)

#Add a new element to an existing set.
a={12,213,32,21,21}
a.add(233)
print(a)

#Remove an element from a set using remove().
a={12,213,32,21,21}
a.remove(21)
print(a)

#Create a set with duplicate values and print the result.
a={12,213,32,21,21}
print(a)

#Find the length of a set.
a={12,213,32,21,67}
print(len(a))

#Use a for loop to print all elements in a set.

a={12,213,32,21,21}
for i in a:
    print(i)

#Check if a number exists in a set using in keyword.
a={12,213,32,21,21}
if 12 in a:
    print("exits")

a={12,213,32,21,21}
for i in a:
    print(i)

#Check if a number exists in a set using in keyword.
a={12,213,32,21,21}
if 12 in a:
    print("exits")


#🟡 Medium (Operations)

#Create two sets and find their union.
a={1,23,32,12}
b={2,23,21,2123}
print(a.union(b))

#Find intersection between {1,2,3} and {3,4,5}.
a={1,2,3} 
b={3,4,5}
print(a.intersection(b))

#Find difference between two sets.
a={1,2,3} 
b={3,4,5}
print(a.difference(b))

#Perform symmetric difference between two sets.
a={1,2,3} 
b={3,4,5}
print(a.symmetric_difference(b))

#Add multiple elements at once using update().
a={1,121,1,1,3434444444}
a.update([34,23,32,2213,12])
print(a)

#Remove an element safely using discard().

#Copy a set using copy() and show that changes to the copy don’t affect the original.