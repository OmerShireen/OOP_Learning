class Rational:
    def __init__(self, numerator:int , denominator:int):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        if denominator < 0:
            numerator , denominator = -numerator , -denominator

        divisor = gcd(numerator,denominator)
        self.__numerator = numerator // divisor
        self.__denominator = denominator // divisor

@property
def numerator(self):
    return self.__numerator

@property
def denominator(self):
    return self.__denominator                 

