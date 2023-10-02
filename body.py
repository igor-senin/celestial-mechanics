from typing import List
from decimal import Decimal
from util import Vector

class Body:
    """
    represents celestial bodies like Moon, Sun or other
    with their parameters like weight or speed
    """
    def __init__(self, 
                 weight: Decimal, 
                 radius: Decimal, 
                 coordinates: List[Decimal], 
                 velocity: List[Decimal],
                 id: int):
        self.weight = weight
        self.radius = radius 
        self.coordinates = Vector(coordinates.copy())
        self.pre_coordinates = Vector(coordinates.copy())
        self.pre_velocity = Vector(velocity.copy())
        self.velocity = Vector(velocity.copy())
        self.id = id

    def __getitem__(self, ind):
        return self.coordinates[ind]

