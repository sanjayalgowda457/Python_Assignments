#Given a number, find the largest number by deleting single digit (order of digits will remain same)
s=input("Enter the number")
n=int(s)
ans = 0
i = 1

while n // i > 0:
        # Remove the least digit
        # after every iteration
        temp = ((n // (i * 10)) * i )+ (n % i)
        i *= 10
        # Store the numbers formed after
        # removing every digit once

        # Compare and store the maximum
        if temp > ans:
            ans = temp

print("The larest number by deleting the single digit of a number",s,"is",ans)