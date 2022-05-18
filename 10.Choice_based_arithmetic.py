#choice based arihmetic
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
choice=int(input("Enter the choice to perform operation:"))
#choice1=addition
#choice2=subtraction
#choice3=multiplys
#choice4=divide
if choice==1:
    add=a+b
    print("Addition: The sum of two numbers",a,b,"is",add)
elif choice==2:
    sub=a-b
    print("subtraction: The difference of two numbers", a, b, "is", sub)
elif choice==3:
    mul=a*b
    print("multiply:The product of two numbers",a,b,"is",mul)
else:
    divide=a/b
    print("Division:The value of divisio of two numbers",a,b,"is",divide)
