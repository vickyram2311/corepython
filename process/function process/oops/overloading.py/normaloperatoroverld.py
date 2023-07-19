#normal method
class operator:
    def __init__(self,a):
        self.a=a
        print(self.a+self.a)
obj=operator(10)
obj1=operator(20)
print("sum",obj.a+obj1.a)