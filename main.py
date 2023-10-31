import turtle

class Point():
    def __init__(self,x:float = None, y:float = None) -> None:
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return f"{self.x}, {self.y}"
    def coords(self) -> list:
        return [self.x,self.y]
    def setX(self,newx):
        self.x = newx
    def setY(self,newy):
        self.y = newy
    def getX(self): return self.x
    def gety(self): return self.y
    
    
p1 = Point()

print(p1)