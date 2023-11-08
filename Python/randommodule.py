import random
#randint()
a=int(input())
b=int(input())
print(random.randint(a,b))
print()



#randrange()
n1=random.randrange(1,5)
print(n1)
print()



#random  choice()
n=int(input())
l=[]
for i in range(n):
    b=int(input())
    l=l+[b]
print(random.choice(l))
print()



#random shuffle()
l=["Nidhi","Sewakram","Manju","Harsh","Amruta"]
random.shuffle(l)
print(l)
print()
    
    
    
#random shuffle with create list
n=int(input())
l=[]
for i in range(n):
    b=input()
    l=l+[b]
    random.shuffle(l)
print(l)
print()




#uniform()
u=random.uniform(3,9)
print(u)
print()

