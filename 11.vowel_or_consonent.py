# Python program to check character is vowel or consonant

ch = input('Enter any character: ')

# check vowel or constant and display result
if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
      or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")