l=[1,1,1,1,1,1,5]
key=l[0]
for i in range(1,len(l)):
    if l[i]==key:
        continue
    else:
        print(l[i])
print("the stray number is",l[i])