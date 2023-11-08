list=["manoj","kala",6,True,13.90,"kala"]
print(list)
print(list[3])
print(list[1:4:1])
print(list.count("kala"))
if True in list:
   print(list.index(True))
else:
   print("object is not found")
list.append("Nidhi")
list.append("Bagde")
print(list)
print(list.pop())
list.pop(3)
print(list)
list.pop()
list.pop()
print(list)
list.insert(2,"hello")
print(list)

#sort function
a=["aman","karan","harsh","samir","sujal"]
a.sort()
print(a)
#reverse()
a.reverse()
print(a)
#copy()
b=a.copy()
print(b)

