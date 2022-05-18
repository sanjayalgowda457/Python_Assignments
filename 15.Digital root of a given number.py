#Digital root of a number
# can be found in Python by doing the sum of all the digits of a given integer
# till a single digit integer is left.
x=int(input("enter a number to find the digital root"))
dr=0
sum=0
if x==0:
    print("the digital sum of 0 is zero(0)")
else:
    n=x
    while(n>0):
        rem=n%10
        dr+=rem
        n=n//10
    print("The Digital sum of the digit ",x,"is",dr)
    if dr==10:
        print("The digital sum of number",x,"is 1")
    else:
        if len(str(dr)) == 2:
            s=x
            while dr>0:
              s = dr % 10
              sum = sum + s
              dr = dr // 10
            print("The Final Digital sum of the digit",x, "after adding all is", sum)
            if sum == 10:
                print("The digital sum of number", x, "is 1")





