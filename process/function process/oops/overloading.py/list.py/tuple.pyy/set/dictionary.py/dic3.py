a={"name":"rk","age":24,"hobby":"chatting","frds":["sam","vicky","vinay"]}
print(a)
b=a.items()
print(b)
#add dict
a["car"]="ignts"
print(b)
#check dict
if "name" in a:
    print("yes,do you have chatting with friends")
    