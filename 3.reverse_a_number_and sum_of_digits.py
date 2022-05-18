# Python Program to Reverse a Number using While loop

Number = int(input("Please Enter any Number: "))
Reverse = 0
sum=0
if Number%10 ==0:
    while (Number > 0):
        Reminder = Number % 10
        Reverse = (Reverse * 10) + Reminder
        sum = sum + Reminder
        Number = Number // 10
    print(" Reverse of entered number is =", "0" + str(Reverse))
    print("sum of the digits is", sum)

else:
    while (Number > 0):
        Reminder = Number % 10
        Reverse = (Reverse * 10) + Reminder
        sum = sum + Reminder
        Number = Number // 10

    print(" Reverse of entered number is =",Reverse)
    print("sum of the digits is", sum)

