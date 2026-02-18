#Print all even numbers between 1 and n.
'''
n=20
for i in range(2,n+1,2):
    print(i)
    
n=40
for i in range(2,n+1):
    if i%2==0:
        print(i)
# Reverse a number using loop.
n=1234
rev=0
for i in range(len(str(n))):
    digit=n%10
    rev=rev*10+digit
    n=n//10
    print(rev)
# Print a Right-Angle Star Pattern
n=5
for i in range(n+1):
    for j in range(i):
        print("*",end="")
    print()
# 9️⃣ Check Whether a Number Is a Palindrome
n=121
temp=n
rev=0
for i in range(len(str(n))):
    digit=n%10
    rev=rev*10+digit
    n=n//10
    if rev==temp:
        print("palindrome",rev)
    else:
        print("Not palindrome",rev)

#Use if, elif, else to compare the number with zero.
n=10
if n>0:
    print("+")
elif n<0:
    print("-")
else:
    print("0")


#  Use modulus operator (%) to check remainder.
n=250
if n%10==0:
    print(n,"is divisible by 10")
#Use for loop with condition num % 2 == 0.
n=20
for num in range(1,n+1):
    if num%2==0:
        print(num) '''
#Use nested loop: outer for rows, inner for stars.
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

