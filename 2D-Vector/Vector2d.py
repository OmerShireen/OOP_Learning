import math
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

    def __add__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        if isinstance(scalar,(int, float)):
            return Vector2D(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        if scalar == 0:
            raise ZeroDivisionError("division by zero")
        return Vector2D(self.x / scalar, self.y / scalar)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def dot (self, other):
        if not isinstance(other, Vector2D):
            raise TypeError("dot product requires another Vector2D")
        return self.x * other.x + self.y * other.y

    def to_tuple(self):
        return (self.x, self.y)

    def normalize(self):
        length = abs(self)
        if length == 0:
            raise ValueError("cannot normalize zerpo vector") 
        return self / length

    def rotate(self, theta):
        """Return a new Vector2D rotated by theta radians (CCW)."""
        cos_t = math.cos(theta)
        sin_t = math.sin(theta)
        x_new = self.x * cos_t - self.y * sin_t
        y_new = self.x * sin_t + self.y * cos_t
        return Vector2D(x_new, y_new)

    def angle(self):
        return math.atan2(self.y, self.x)
         

                                              

