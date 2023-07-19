class bird:
    def sound(self):
        print("cuckoo")

    def fly(self):
        print("its always flying in sky")

class bird1(bird):
    def cocktail(self):
        print("cutiee")

class bird2(bird):
    def lovebirds(self):
        print("symbol of love")

obj1=bird()
obj2=bird1()
obj3=bird2()
obj1.sound()
obj1.fly()
obj1.sound()
obj2.cocktail()
obj1.sound()
obj3.lovebirds()