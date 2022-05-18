#program to find the largest of three numbers
#taking the user inputs
num1 = int(input("enter num1:"))
num2 = int(input("enter num2:"))
num3 = int(input("enter num3:"))
#to find the largest using nested if statement
if (num1>=num2)and (num1>=3):
    largest=num1
elif(num2>=num1)and(num2>=num3):
    largest=num2
else:
    largest=num3

print("The Largest Number is:",largest)