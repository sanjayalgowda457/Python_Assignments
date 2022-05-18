x=[1,50,40,12,30,50,40]
x.sort()
print("The sorted list is:",x)
y=sum(x)
print("The sum of the elements in the list is",y)
l=len(x)
print("The total no of elements in the list is",l)
mean=y/l
print("The mean is",mean)
count=0
print("The elements smaller than its mean are:")
for i in range(len(x)):
    if x[i]<mean:
        print(x[i])
        count+=1
    else:
        break
print("The no of elements smaller than mean are:",count)