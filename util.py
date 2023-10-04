from math import sqrt
from decimal import *
from typing import List


"""
n-dimensional vector
Uses Decimal class
"""
class Vector:
    def __init__(self, coords: List[Decimal]):
        self.coords = list(coords)

    def __getitem__(self, index):
        return self.coords[index]

    def __repr__(self):
        return '(' + ', '.join(str(c) for c in self.coords) + ')'

    def __str__(self):
        return '(' + ', '.join(str(c) for c in self.coords) + ')'

    def __neg__(self):
        self.coords = self.coords * (-1)

    def __add__(self, other):
        other = Vector(other)
        assert len(self.coords) == len(other.coords), "__add__ different dimentions\n"
        r = [self[i] + other[i] for i in range(len(self.coords))]
        return Vector(r)

    def __iadd__(self, other):
        assert len(self.coords) == len(other.coords), "__add__ different dimentions\n"
        other = Vector(other)
        for i, value in enumerate(other.coords):
            self.coords[i] += value
        return self

    def __isub__(self, other):
        self.__iadd__(-Vector(other))

    def __sub__(self, other):
        other = Vector(other)
        assert len(self.coords) == len(other.coords), "__add__ different dimentions\n"
        r = [self[i] - other[i] for i in range(len(self.coords))]
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
        if type(other) != type(self):
            return Vector([self[i] * other for i in range(len(self.coords))])
        return Vector([self[i] * other[i] for i in range(len(self.coords))])

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        other = Decimal(other)
        return Vector([self[i] / other for i in range(len(self.coords))])

    def Norm(self):
        return self.NormSquared().sqrt()

    def NormSquared(self):
        return sum([c**2 for c in self.coords])

    def Dist(self, other):
        other = Vector(other)
        return (self - other).Norm()

getcontext().prec = 80

v_1 = Vector([Decimal(1), Decimal(2), Decimal(3)])
v_2 = Vector([Decimal(3), Decimal(2), Decimal(1)])
v_3 = v_1 - v_2

a = Decimal(-1)
print("positive ", v_1, "negative", v_1 * (-1))
print(v_1, " add ", v_1, "equal", v_1 + v_1)
print(v_1, " sub ", v_1, "equal", v_1 - v_1)
print(v_1, " mul ", v_1, "equal", v_1 * v_1)
print(v_1, " div ", (-2), "equal", v_1 / Decimal(-2))
print(v_1, " norm_squared ", v_1.NormSquared())
print(v_1, " norm ", v_1.Norm())
v_5 = v_4 = v_1
v_5 += v_2 
print(v_4, " += ", v_2, " equals ", v_5)


print(v_3.Norm())

print(v_1.Dist(v_2))

print(v_1, v_2, v_3)
