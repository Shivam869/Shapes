class square:
    def __init__(self,side):
        self.side=side
    def display(self):
        print("Side: ",self.side)
        print("Perimeter: ",self.side*4)
        print("Area: ",self.side**4)
        self.side=18
class rectangle:
    def __init__(self,length , side):
        self.lenght=length
        super().__init__(side)
        self.lenght=24
obj=rectangle
obj.display()
