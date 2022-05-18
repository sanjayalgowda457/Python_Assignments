n = int(input("Please enter the start number: "))
m = int(input("Please enter the end number: "))
count = 0
print("prime numbers between ",n,"and",m,"are")
for i in range(n,m):
    if i > 1:
        for j in range(2,i):
            if(i % j == 0):
                break
        else:
            print(i) #ToDisplay prime number


            count = count + 1
print("Total prime numbers between",n, "and",m, "are",count)