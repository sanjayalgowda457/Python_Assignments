#Check whether given string is isogram or not
#An Isogram is a word in which no letter occurs more than once.
s=input("Enter the string: ")
s.lower()
g=0
for i in s:
    if (s.count(i)>1):
        g+=1
if g==0:
    print("The entered String",s," is a ISOGRAM ")
else:
    print("The entered String",s," is not a ISOGRAM ")

