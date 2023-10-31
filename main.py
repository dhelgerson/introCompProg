import turtle

class Point():
    def __init__(self,x:float = None, y:float = None) -> None:
        self.x = x
        self.y = y
        return self.coords()
    def __str__(self) -> str:
        return f"{self.x}, {self.y}"
    def coords(self) -> list:
        return [self.x,self.y]
    
p1 = Point()

print(p1)