a=[10,20,30,40,50]
for i in range(len(a)):
    print(a[i])
print()



i=1
l=[]
while(i<11):
   n=input()
   l=l+[n]
   i=i+1
print(l)
print()




n=int(input())
l=[]
for i in range(n):
   m=input()
   l=l+[m]
print(l)
print()


j=int(input())
l=[]
for a in range(j):
    b=input()
    l=l+[b]
print(l[-1: :-1])
print()


#creat list with append function
l=[]
for a in range(1,31):
    l.append(a)
print(l)
print()


#list comprehension
n=[h for h in range(1,101) if h%2==0]
print(n)
































   

