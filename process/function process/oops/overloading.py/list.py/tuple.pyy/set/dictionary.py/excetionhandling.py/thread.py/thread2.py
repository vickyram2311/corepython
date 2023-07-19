from threading import*

class booking(Thread):
    def __init__(self,mn=""):
        super().__init__()
        self.name=mn
        self.__total=50

    def run(self):
        print("welcome",self.name,"to inox multiplex")
        required=int(input("tell as req ticket"))
        if required<=self.__total:
            self.__total-=required
            print(required,"ticket has issued",self.name)
        else:
            print("available is",self.__total)

b1=booking("suresh")
b2=booking("vikas")
b3=booking("balaji")

b1.start()
b1.join()
b2.start()
b2.join()
b3.start()


