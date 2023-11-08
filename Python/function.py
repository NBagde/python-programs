#create simple function
def hello():
    print("Hello word")
hello()
hello()
hello()


#create functin with arguments
def hii(a,b):
   print(a*b)
a=int(input())
b=int(input())
hii(a,b)
print()




#create function argument with default value
def sum(a,b=5):
    print(a+b)
a=int(input())
b=int(input())
sum(a,b)
sum(a)
print()



#How to return statement use in function
def cross(a,b):
    c=a*b
    return c
m=int(input())
n=int(input())
d=cross(m,n)
print(d)
print()




def trio(a,b,c):
    d=a+b+c
    return d
m=int(input())
n=int(input())
o=int(input())
e=trio(m,n,o)
print(e)
print()



#square()
def squr(a):
    c=a*a
    return c
b=int(input())
d=squr(b)
print(d)
print()



















   
