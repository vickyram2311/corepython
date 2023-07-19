#same name same parameter
class sam:
    def name(self):
        print("vicky")
class raja(sam):
    def name(self):
        super().name()
        print("kumar")
class arun(raja):
    def name(self):
         super().name()
         print("devi")
a=arun()
a.name()