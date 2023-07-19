try:
    ss={"name":"sam","name1":"pk"}
    print(ss["age"])
except KeyError as e:
    print("key error",e)

#attribute error
try:
    class a:


        pass
    A=a()
    a.hello()
except AttributeError as e:
    print("attribute error:",e)
    