#single inheritance 

class bike:
    def gear(self):
        print("5 speed gear box")
class car(bike):
    def benz(self):
        print("its a costly car")

c=car()
c.benz()
c.gear()