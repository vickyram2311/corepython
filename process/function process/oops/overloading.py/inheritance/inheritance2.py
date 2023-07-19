#multilevel inhertance

class bank:
    def name(self):
        print("axis bank")
class bank1(bank):
    def name1(self):
        print("hdfc bank")
class bank2(bank1):
    def name2(self):
        print("icici bank")

b=bank2()
b.name()
b.name1()
b.name2()