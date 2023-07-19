from threading import *
from time import sleep

class React(Thread):
    def __init__(self,nm=""):
        super().__init__()
        self.name=nm
        self.clicks=[23,23,44,55,66,77,88,99,10,]
    def run (self):
        print("welcome",self.name)

        for x in self.clicks:
            print(x)
            sleep(2)

r1=React("annamalai")
r2=React("sabari")
r3=React("manoj")

r1.start()
r1.join()
r2.start()
r2.join()
r3.start()
