#program to find the largest of three numbers
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
num3=int(input("enter num3:"))
num4=int(input("enter num4:"))
#to find the largest using nested if statement
if (num1>=num2)and (num1>=3)and(num1>=num4):
    largest=num1
elif(num2>=num1)and(num2>=num3)and(num2>=num4):
    largest=num2
elif(num3>=num1)and(num3>=num2)and(num3>=num4):
    largest=num3
else:
    largest=num4

print("The Largest Number is:",largest)