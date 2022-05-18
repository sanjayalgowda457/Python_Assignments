s=input("Enter a string: ")
new=[]
for i, val in enumerate(s[:]):
    up=s[i].upper()
    c=s[:i] + up + s[i+1:]
    new.append(c)
print("The Mexican wave of the given string",s,"is",new)