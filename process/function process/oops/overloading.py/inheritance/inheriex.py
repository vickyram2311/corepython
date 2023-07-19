class college:
    def name(self):
        print("vysya")

class college1:
    def name1(self):
        print("avs")

class main(college,college1):
    def vvv(self):
        print("both are nice college")

m=main()
m.name()
m.name1()
m.vvv()