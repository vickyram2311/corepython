bio={"name":"vicky","age":24,"native":"salem"}
print(bio)
#clear method
bio.clear()
print(bio)
#copy method
bio={"name":"vicky","age":24,"native":"salem"}
a=bio.copy()
print(a)
#get method
a=bio.get("native")
print(a)
a=bio.get("car","alto")
print(a)
#items method
a=bio.items()
print(a)
#key method
a=bio.keys()
print(a)
a=bio.keys()
bio["hobby"]="chatting"
print(a)
#pop
bio.pop("age")
print(bio)
a=bio.pop("name")
print(a)
#pop items
bio={"name":"vicky","age":24,"native":"salem"}
print(bio)
bio.popitem()
print(bio)
#set default
a=bio.setdefault("frnds","pp")
print(a)
#update
bio.update({"car":"alto"})
print(bio)
#values
a=bio.values()
print(a)
a=bio.values()
bio["car"]="pk"
print(a)
