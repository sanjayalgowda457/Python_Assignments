#Generate accumulated strings,e.g. abcd ==> A-Bb-Ccc-Dddd
s=input("enter the string")
s.split()
l=list(s)
y=[]
print(s)
for i in range(len(l)):
    l[i]=l[i]*(i+1)
    y.append(l[i])
z=str(y)
print(z)
print("The generated accumulated strings are", z)