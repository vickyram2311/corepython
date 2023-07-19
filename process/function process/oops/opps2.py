class movie:
    def __init__(self,name,year):
        self.N=name;
        self.Y=year;
    def print(self):
        print(self.N,self.Y)
ans=movie("thunivu",2023)
ans.print()