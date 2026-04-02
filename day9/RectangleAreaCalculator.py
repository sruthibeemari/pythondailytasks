class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print("Area= ",self.length*self.width)

r=rectangle(8,9)
r.area()
