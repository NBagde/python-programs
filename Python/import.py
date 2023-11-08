import random
a=random.randint(1,100)
b=int(input("Enter a number:"))
while(a!=b):
     if(a==b):
        print("You Won, congratulation\n")
     elif(b>a):
        print("The number is too big\n")
     elif(b<a):
        print("The number is too small\n")
     else:
        b=int(input("Enter a number:"))
        
