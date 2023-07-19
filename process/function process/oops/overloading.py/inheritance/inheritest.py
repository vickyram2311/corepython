class bike:
    def name(self):
        print("bike is fast")

class bikemodel:
    def neme1(self):
        print("pulsar220")

class bikeclr:
    def name2(self):
        print("black")

class topspeed(bike,bikemodel,bikeclr):
    def name3(self):
        print("170")

t=topspeed()
t.name()
t.neme1()
t.name2()
t.name3()