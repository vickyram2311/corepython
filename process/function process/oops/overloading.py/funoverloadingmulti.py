#overloading with multiple arguments passing
class multiple:
    def add(self,*args):
        sum=50;
        for i in args:
            sum+=i
        print("add values:",sum)

m=multiple()
m.add(20)
m.add(40,50)
m.add(40,50,100)