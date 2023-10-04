from typing import List
from decimal import Decimal
import numpy as np

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
        self.coordinates = coordinates
        self.pre_velocity = velocity
        self.velocity = velocity
        self.id = id

    def __getitem__(self, ind):
        return self.coordinates[ind]

