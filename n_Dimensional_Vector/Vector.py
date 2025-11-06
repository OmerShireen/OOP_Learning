import math 
from copy import deepcopy
class Vector:
    def __init__(self, data=3):
        if isinstance(data, Vector):
            self._coords = deepcopy(data._coords)
        elif isinstance(data, int):
            self._coords = [0] * data
        elif isinstance(data, list):
            self._coords = [float(x) for x in data]
        else:
            raise TypeError("Vector must be created with int, list, or another Vector")

    @property
    def coords(self):
        return self._coords

    @coords.setter
    def coords(self, values):
        if len(values) != len(self._coords):
            raise ValueError("New values must match vector dimension")
        self._coords = [float(v) for v in values]

    def __len__(self):
        return len(self._coords)  

    def __getitem__(self, j):
        if j < -len(self) or j  >= len(self):
            raise IndexError(f"Index {j} out of range for vector of dimension {len(self)}")
        return self._coords[j]

    def __setitem__(self, j, value):
        if j < -len(self) or j >= len(self):
            raise IndexError(f"Index {j} out of range for vector of dimension {len(self)}")
        self._coords[j] = value 

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Dimension must be same")

        result = Vector((len(self)))
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return result    

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("Dimensions must be same")

        result = Vector((len(self)))
        for i in range(len(self)):
            result[i] = self[i] - other[i]
        return result 

    def __mul__(self, scalar):
        if not isinstance(scalar, (int,float)):
            raise TypeError("Must be multiplied by scalar number")

        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] * scalar 
        return result

    def __abs__(self):
        result = 0
        for i in range(len(self)):
            result += self[i] ** 2
        return result ** 0.5

    def __eq__(self, other):
        if not isinstance(other, vector):
            return False
        if len(self) != len(other):
            return False
        for j in range(len(self)):
            if self[j] != other[j]:
                return False
        return True

    def __ne__(self, other):
       return not self == other
    
    def __str__(self):
        return f"<{str(self._coords)[1:-1]}"

    def __repr__(self):
        return f"Vector({self._coords!r})"    
    