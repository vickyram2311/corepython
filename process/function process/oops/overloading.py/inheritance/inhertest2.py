class friends:
    def name(self):
        print("vasanth")
class friends1(friends):
    def name1(self):
        print("magi")
class friends2(friends1):
    def name2(self):
        print("vicky")

f=friends2()
f.name()
f.name1()
f.name2()