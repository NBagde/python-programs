'''
a={"nidhi","amruta","lalita","harsh"}
a.update(["india","china","neo"])
print(a)
'''

b={"hii", "hlw", "god tusi great ho", "remains"}
b.update(["minal","kavya","ruksan"])
print(b)
print(b.pop())
b.remove("remains")
print(b)

#Union function
a={"nidhi","sewakram","manju","harsh"}
b={"karan","harsh","amruta","kavita"}
print(a.union(b))
#intersection()
print(a.intersection(b))
#difference()
print(a.difference(b))
print(b.difference(a))
print(a.union(b))
#symmetric difference()
print(a.symmetric_difference(b))
print(a.union(b))
