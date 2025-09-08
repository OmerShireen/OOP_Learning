class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def __add__(self,other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point :{self.x} , {self.y} "


p1 = Point(55,60)
p2 = Point(15,20)
p3 = p1 + p2 

print(p1)
print(p2)
print(p3)