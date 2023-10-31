import turtle

class Point():
    def __init__(self,x:float = None, y:float = None) -> None:
        self.x = x
        self.y = y
        pass
    
p1 = Point()

print(p1.x,p1.y)