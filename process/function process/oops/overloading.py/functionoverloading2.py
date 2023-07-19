#same name differnt parameters
class over:
    def load(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None:
            return a+b
        else:
            return a
o=over()

print("sum",o.load(10))
print("sum",o.load(10,20))
print("sum",o.load(10,20,30))
