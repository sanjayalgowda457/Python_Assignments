#the sum of triangular element is (n*(n+1))/2
n=int(input("enter the number: "))
sum=0
print("The terms to add is")
for i in range(1, n + 1):
        sum1= i * (i + 1) / 2
        print(int(sum1))
        sum+=sum1
print("The Total Sum of the Triangular number",n,"is",int(sum))