l=[300,20,30,40,50,95,45]
sum=sum(l)
len=len(l)
mean=sum/len
print("The mean of a list of elements",l,"is",mean)
for i in range(len):
    if mean in l:
        continue
    l+=[mean]
l.sort()
for i in range(len):
    if l[i]==mean:
        print("The numbers closest to the mean:",mean,"is",l[i-1],l[i+1])
    else:
        continue
