#to check whther the enterd year is leap year or not
n=int(input("enter a year:"))
#%4will check for leap year
if (n%400==0) and (n%100 !=0)or(n%4==0):#%400will check for the remainder as 0, and %100check for century  year

    print("The entered year",n," is aleap year")
else:
    print("The entered year",n,"is not a leap year")