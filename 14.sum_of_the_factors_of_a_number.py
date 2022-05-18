n=int(input("enter the number :"))
sum=0
if n==0:
    print("Enter the non zero value")
else:
    print("The factors of a number",n,"is")
    for i in range(1,n+1):
        if n%i==0:
            print(i)
            sum+=i
print("The sum of factors of number",n,"is",sum)