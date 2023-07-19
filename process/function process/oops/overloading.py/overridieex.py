class parent:
    def name(self):
        print("ram")

class family(parent):
    def name(self):
        super().name()
        print("kalai")

class overall(family):
    def name(self):
        super().name()
        print("vicky")

o=overall()
o.name()