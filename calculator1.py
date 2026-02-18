
print("Please select operation -\n1.Add\n2.Subtract\n3.Multiply\n4.Divide")

num=(input("Select the suoperation (1-4):"))
a=int(input("Enter the first numbers:"))
b=int(input("Enter the second numbers:"))
if num=="addition":
    print(a,"+",b,"=",a+b)
elif num =="subtract":
    print(a,"-",b,"=",a-b)
elif num=="multiply":
    print(a,"*",b,"=",a*b)
elif num=="division":
    print(a,"/",b,"=",a/b)
else:
    print("invalid input,once check the operation number")

    
    