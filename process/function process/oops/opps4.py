class car:
    cname="benz"
    def __init__(self,name):
        self.name = name
    def luxury(self):
        print("its a costly car for{}".format(self.name))

c=car("bmw");
c1=car("ss");
c.luxury()
c1.luxury()
