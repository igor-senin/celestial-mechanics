from math import sqrt
from decimal import *


"""
n-dimensional vector
Uses Decimal class
"""
class Vector:
    def __init__(self, coords):
        self.coords = list(coords)

    def __getitem__(self, index):
        return self.coords[index]

    def __repr__(self):
        return '(' + ', '.join(str(c) for c in self.coords) + ')'

    def __str__(self):
        return '(' + ', '.join(str(c) for c in self.coords) + ')'

    def __add__(self, other):
        other = Vector(other)
        r = [self[i] + other[i]
             for i in range(min(len(self.coords), len(other.coords)))]
        return Vector(r)

    def __sub__(self, other):
        other = Vector(other)
        r = [self[i] - other[i]
             for i in range(min(len(self.coords), len(other.coords)))]
        return Vector(r)

    def __eq__(self, other):
        other = Vector(other)
        if len(self.coords) != len(other.coords):
            return False
        for i in range(len(self.coords)):
            if self[i] != other[i]:
                return False
        return True

    def __ne__(self, other):
        return not self == other

    def __mul__(self, other):
        other = Vector(other)
        if type(other) != type(self):
            return Vector([self[i] * other for i in range(len(self.coords))])
        return Vector([self[i] * other[i]
                       for i in range(min(len(self.coords), len(other.coords)))])

    def __rmul__(self, other):
        return self * other

    def __div__(self, other):
        if type(other) != Decimal:
            raise TypeError('Vector accepts only Decimals')
        return Vector([self[i] / other
                       for i in range(len(self.coords))])

    def Norm(self):
        return sum([c**2 for c in self.coords]).sqrt()

    def Dist(self, other):
        other = Vector(other)
        return (self - other).Norm()

getcontext().prec = 80

v_1 = Vector([Decimal(1), Decimal(2), Decimal(3)])
v_2 = Vector([Decimal(3), Decimal(2), Decimal(1)])
v_3 = v_1 - v_2

print(v_3.Norm())

print(v_1.Dist(v_2))

print(v_1, v_2, v_3)
