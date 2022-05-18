onboard=[10,60,80,70,50]
alighting=[20,30,10,5,15]
present=0
print("total onboarded people:",sum(onboard))
print("total alighted people :",sum(alighting))
if len(onboard)==len(alighting):
    for i in range(len(onboard)):
        present +=onboard[i]-alighting[i]
else:
    print("both the arrays should be of same lengths")
print("The no of people's present in the Bus at the end is:",present)