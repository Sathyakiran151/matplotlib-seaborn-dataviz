# 🟢 Easy

# Print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)


# Print even numbers between 1 and 20 using a while loop.
i =1
while i<20:
    if i%2==0:
        print("it is even",i)    
    i+=1

# Print the multiplication table of 5.
a = int(input("multiplication of  :"))
for i in range(1,11):
    print(a,"X",i ,"=",a*i)

# Sum numbers from 1 to 100.

# Print characters of a string using a loop.
a = "sathya is a vibe coder "
for i in a:
    print(i,end = "")

""" 
*
**
***
****
*****"""
n =5
for i in range (1,n+1):
    for j in range(1,i+1):
        print("* ",end = "")
    print()

'''
*****
****
***
**
* 
'''
n=5

for i in range(1,n+1):
    for j in range(0,n+1-i):
        print("*",end=" ")
    print()
'''
11111
22222
33333
44444
55555'''
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=" ")
    print()

'''
12345
12345
12345
12345
12345'''
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()

'''
1
12
123
1234
12345'''
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
'''
1
22
333
4444
55555'''
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

'''
1
11
111
1111
11111'''
n=5
for i in range(1,n+1):
    num=1
    for j in range(1,i+1):
        print(num,end=" ")
    print()
'''
1
13
135
1357
ODD NUMBERS'''
n=5
for i in range(1,n+1):
    num=1
    for j in range(1,i+1):
        print(num,end=" ")
        num+=2
    print()
'''
2
24
246
2468
EVEN NUMBERS'''
n=5
for i in range(1,n+1):
    num=2
    for j in range(1,i+1):
        print(num,end=" ")
        num+=2
    print()

'''
A
AA
AAA
AAAA
AAAAA'''
n=5
for i in range(1,n+1):
    num=65
    for j in range(1,i+1):
        print(chr(num),end=" ")
    print()
'''
A
BB
CCC
DDDD
EEEEE'''
n=4
for i in range(0,n+1):
    for j in range(0,i+1):
        print(chr(65+i),end=" ")
    print()

'''
A
AB
ABC
ABCD
ABCDE
'''
n=4
for i in range(0,n+1):
    for j in range(0,i+1):
        print(chr(65+j),end=" ")
    print()

'''
55555
4444
333
22
1
'''
n=5
for i in range(5,0,-1):
    for j in range(i):
        print(i,end="")
    print()

'''
12345
1234
123
12
1
'''
n=5
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

'''
1
21
321
4321
54321
'''
n=5
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end="")
    print()

'''
54321
4321
321
21
1
'''
n=5
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()

'''
     *
    **
   ***
  ****
 *****
'''
n=5
for i in range(1,n+1):
    for j in range(5,i,-1):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    print()
'''
11111
2222
333
44
5

'''

n=5
for i in range(1,n+1):
    for j in range(5,i-1,-1):
        print(i,end="")
    print()

''' 
12345
1234
123
12
1
      
'''
n=5
for i in range(1,n+1):
    for j in range(1,n+1-i+1):
        print(j,end="")
    print()

''' 
1
2 3
4 5 6
7 8 9 10
      
'''
n=4
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()
