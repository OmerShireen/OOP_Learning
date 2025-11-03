class Vector2D:
    def __init__(self, x, y):
        self._x = float(x)
        self._y = float(y)


    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = float(value)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = float(value)

    def __repr__(self):
        return f"Vector2D({self.x},{self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"    

