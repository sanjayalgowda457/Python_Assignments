n=int(input("Enter a number to find the factorial: "))
factorial=1
if n < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif n==0 or n==1:
    print("The factorial of ",n,"is: 1")
else:
    for i in range(2,n+1):
        factorial=factorial*i
    print("The factorial of",n, "is", factorial)
