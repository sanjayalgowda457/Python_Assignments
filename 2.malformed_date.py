#"45/8/2018" to "14/9/2018"
x=input("enter the no of days")
y=input("enter the no of months")
if y==4 or y==6 or y==8 or y==10 or y==12:
    s=30
elif y==2:
    s=28
else:
    s=31
z=input("enter the year ")
print("the entered details are:",x,"/",y,"/",z)
p=int(z)
q=int(y)
r=int(x)

#assume that each month of 30days
# Assume that years is
# of 365 days
number_of_days=((p*365)+(q*s)+r)
year = int(number_of_days / 365)
month = int((number_of_days % 365) /s)
days = int(number_of_days % 365) % s

print("years = ", year,
      "\nmonth = ",month,
      "\ndays = ", days)
print("The value of malformed date is","%02d/%02d/%02d"%(days,month,year))
