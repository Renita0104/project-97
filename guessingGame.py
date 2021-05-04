import random
rd=random.randint(0,5)
for i in range(1,5):
    nos=int(input('Enter any number from 1-9'))
if rd==nos:
   print('you are correcr')
else:
   print("you are wrong")