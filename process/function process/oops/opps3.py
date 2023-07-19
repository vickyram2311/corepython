#class and object with class and instance attributes

class a:
    name="raja"
    def __init__(self,ss1):
        self.ss1=ss1

obj1=a("sam")
obj2=a("god")
print("boy is playing{}".format(obj1.__class__.name));
print("love is{}".format(obj2.__class__.name));
print("car is{}".format(obj1.ss1))
print("name is{}".format(obj2.ss1))
