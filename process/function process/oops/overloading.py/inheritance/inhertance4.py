class college:
    def name(self):
        print("college is good")

class clgname:
    def name1(self):
        print("vysya college")

class clglocation:
    def name2(self):
        print("ayothoiyapattinam")

class placement(clgname,clglocation,college):
    def name3(self):
        print("good")

p=placement()
p.name()
p.name1()
p.name2()
p.name3()