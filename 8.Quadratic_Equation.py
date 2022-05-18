# Python Program to find roots of a Quadratic Equation
a = int(input('Enter value of a :'))
b = int(input('Enter value of b :'))
c = int(input('Enter value of c :'))
#check for value of a
if a == 0:
    print("a cannot be zero")
#if a is greater than 0
else:
    #to calculate the value
    val = b**2 - 4 * a * c
    root = val**0.5
    #Check for roots and print according to their nature
    if val > 0:
        print("Two Real Roots are :")
        print((-b + root)/(2 * a))
        print((-b - root)/(2 * a))
    elif val == 0:
        print("both the roots are same, and  the value is: ")
        print(-b / (2*a))
    else:
        print("complex roots and both are distinct,and the values are:")
        print(- b / (2*a) , " + i", root)
        print(- b / (2*a) , " - i", root)