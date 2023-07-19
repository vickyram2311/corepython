#multiple inheritance

class travels:
    def name (self):
        print("rk travels")
class travels1:
    def name1 (self):
        print("kpm travels")
class main(travels,travels1):
    def luxary(self):
        print("enjoy the ride")

m=main()
m.name()
m.name1()
m.luxary()