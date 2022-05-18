#to take the user input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if(num1 > num2):
    lcm = num1
else:
    lcm=num2

while(True):
    if((lcm % num1 == 0) and (lcm % num2 == 0)):
        print("The L.C.M. of", num1,"and", num2,"is", lcm)
        break
    lcm += 1