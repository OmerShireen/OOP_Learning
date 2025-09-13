from math import gcd

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


    def __add__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Rational(num, den)              


    def __sub__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator 
        return Rational(num, den)  


    def __mul__(self, other):
        if not isinstance(other, Rational):
           return NotImplemented
        num = self.numerator * other.numerator 
        den = self.denominator * other.denominator
        return Rational(num, den)


    def __truediv__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        if self.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator 
        return Rational(num, den)    

    def __eq__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return self.numerator == other.numerator and self.denominator == other.denominator       

    def __float__(self):
        return self.numerator / self.denominator

    def __str__(self):
        if self.denominator == 1:
           return f"{self.numerator}"
        return f"{self.numerator}/{self.denominator}"                          


