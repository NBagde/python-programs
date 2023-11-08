#empty dictionary
a={}
b=dict()
print(type(a))
print(type(b))

#dict with some value
a={"firstname": "nidhi", "lastname": "Bagde"}
print(a)
a.pop("lastname")
print(a)
print(a.keys())
print(a.values())
print(a.items())
for key,values in a.items():
   print(key,values,sep="-")

#adding/updating data in dictionary
c={"username":"Harsh","password":"Nidhi123"}
c['age']=24
c['password']="harsh123"
print(c)
print(c.get("password"))


