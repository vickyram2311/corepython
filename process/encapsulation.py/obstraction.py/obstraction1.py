
#hiding the data but showing the functionality

from abc import ABC
class bus(ABC):
    def volvo(self):
        print("hello")
        pass

class srt(bus):
    def volvo(self):
        print("nice one")

class kpn(bus):
    def volvo(self):
        print("ac bus")

class rkv(bus):
    def volvo(self):
        print("luxary bus")

s=srt()
s.volvo()
s1=rkv()
s1.volvo()
b=bus()
b.volvo()
s2=kpn()
s2.volvo()