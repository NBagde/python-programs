import random
n=int(input("Enter a number:"))
Cnumber=random.randrange(1,101)
if(n>Cnumber):
    print("Computer generated number:",Cnumber)
    print("your guess number is high")
elif(n<Cnumber):
    print("Computer generated number:",Cnumber)
    print("your guess number is low")
else:
    print("Computer generated number:",Cnumber)
    print("your guess number is equal")
    
