import module1
a=int(input())
b=int(input())
print(module1.sum(a,b))
print()



#use alias in module it means ye module ke nam ko chota krta hai
import module1 as m
a=int(input())
print(m.sqr(a))
print()



#this is another part to import module
from module1 import sqr
print(sqr(10))
print()


