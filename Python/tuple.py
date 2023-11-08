t=(10,20,30,40,50)
a=t[3]
print(a)
print()


a=(10,20,30,40,50)
for i in range(len(a)):
    print(a[i])
print()



b=(34,56,78,90,32)
print("The minimum element of in the tuple:",min(b))
for a in b:
    print(a)
print()





t=(24,56,78,98,54,67,24,12,24)
print("The minimum value is:",min(t))     #min()
print()
print("The maximum value is:",max(t))     #max()
print()
c=t.count(24)                             #count()
print("The count of the number:",c)
print()
b=t.index(98)                             #index()    
print("The Index of the number is:",b)
print()
print("The sum of the all element is:",sum(t))                              #sum()
print()




h=(4,5,6,8,2)
print(sum(h,20))                      #sum with default value
print()



