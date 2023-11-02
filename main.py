from __future__ import annotations
import turtle

class Point():
    def __init__(self,x:float = None, y:float = None, color = 'green') -> None:
        self.x = x
        self.y = y
        self.t = turtle.Turtle()
        self.t.color(color)
        self.t.goto(self.x,self.y)
        
    def pos(self) -> tuple:
        return self.x, self.y
    def __str__(self) -> str: return f"{self.x}, {self.y}"
    def __mul__(self,divisor):
        return Point(self.x / divisor, self.y / divisor)
    def coords(self) -> list: return [self.x,self.y]
    def setX(self,newx): self.x = newx
    def setY(self,newy): self.y = newy
    def getX(self): return self.x
    def gety(self): return self.y
    def getMidpointBewteen(self, other:Point) -> Point:
        """returns a Point who's location is the midpoint between self and other

        Args:
            other (Point): other point

        Returns:
            Point: Midpoint
        """
        return Point((self.x + other.y) / 2, (self.y + other.y) / 2)
    
    
if __name__ == '__main__':
    p1 = Point(1,1)
    p2 = Point(2,2)
    print(p1.getMidpointBewteen(p2))