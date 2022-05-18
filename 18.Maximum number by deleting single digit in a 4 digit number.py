n=int(input("Enter the number"))
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

print(ans)