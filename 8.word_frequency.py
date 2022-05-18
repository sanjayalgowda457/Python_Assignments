#Compute the word frequency in given message
# break the string into list of words
str=input("Enter a list of words")
str = str.split()
str2 = []

# loop till string values present in list str
for i in str:

    # checking for the duplicacy
    if i not in str2:
        # insert value in str2
        str2.append(i)

for i in range(0, len(str2)):
    # count the frequency of each word(present
    # in str2) in str and print
    print('Frequency of', str2[i], 'is :', str.count(str2[i]))