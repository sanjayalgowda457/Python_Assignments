n=int(input("enter the value of n: "))
r=int(input("enter the value of r: "))
n_fact=1
r_fact=1
s_fact=1
if n < 0:
   print("Sorry, the combination does not exist for negative numbers")
elif n==1 and r==0:
    print("The value of the combination of ",n,"C",r,"is: 1")
else:
    for i in range(2,n+1):
        n_fact=n_fact*i
    print("The factorial of",n, "is", n_fact)
    for j in range(2,r+1):
        r_fact=r_fact*j
    print("The factorial of", r, "is", r_fact)
    s=n-r
    for k in range(2,s+1):
        s_fact=s_fact*k
    print("The factorial of n-r is", s_fact)

    nCr=(n_fact/(s_fact*r_fact))
    print("The Value of the given combination nCr:",n,"C",r,"is",int(nCr))

