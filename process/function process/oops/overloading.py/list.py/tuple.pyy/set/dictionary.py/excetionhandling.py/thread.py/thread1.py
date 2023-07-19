"""Multithread:
concurrent Process
thread
class derived(thread):
    def run():
        thread execution point 
name>>name of the thread
function:
     Start 
     sleep
     aquire
     release
     join
single task Multithread
multi task Multithread"""

from threading import*

class fista(Thread):
    def __init__(self,nm=""):
        super().__init__()
        self.name=nm
    def run(self):
        print("welcome",self.name)

f1=fista("suresh")
f2=fista("mani")
f3=fista("dev")

f1.start()
f2.start()
f3.start()
