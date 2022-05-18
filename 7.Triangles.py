x=int(input("enter the base dimension of triangle:"))
y=int(input("enter the side dimension of triangle:"))
z=int(input("enter the hypotenuse side of the triangle:"))

#for Equilateral triangle:all the sides are equal
if x == y == z:
    print("\nThe entered Triangle is Equilateral Triangle")

    # for isoceles triangle:only two sides are equal
elif x == y or y == z or z == x:
    print("\nThe entered triangle is Isoceles Triangle")

# Otherwise scalene triangle: whr all the sides are different
else:
    print("\nThe entered Triangle is Scalene Triangle")
#to find the Right angled Triangle
if (x*x + y*y == z*z)or(y*y + z*z ==x*x)or(z*z + x*x ==y*y):
    print("\nThe Entered Triangle is a Right angled Triangle")

else:
    print("\n The entered triangle is not a Right angled Triangle")

