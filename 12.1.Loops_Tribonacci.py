n=int(input("Enter the no of terms:"))
n1=0
n2=0
n3=1
count=0

#checking for no of terms
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Tribonacci sequence upto",n,":")
   print(n1)
elif n == 2:
    print("Tribonacci sequence upto",n,"terms is:",n1,n2)
elif n==3:
    print("Tribonacci sequence upto", n, "terms is:", n1, n2,n3)
else:
    print("Tribonacci sequence of:",n,"terms is:")
    while count < n:
        print(n1)
        nth = n1 + n2 +n3
        # update values
        n1 = n2
        n2 = n3
        n3=nth
        count += 1