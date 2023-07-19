class friend:
    def vicky(self):
        print("unlucky man")

class friend1:
    def vinay(self):
        print("nice looking guy")

class hello(friend,friend1):
    def dash(self):
        print("both are friends")

m=hello()
m.vicky()
m.vinay()
m.dash()