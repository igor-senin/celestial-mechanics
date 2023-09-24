from typing import List

class Body:
    """
    represents celestial bodies like Moon, Sun or other
    with their parameters like weight or speed
    """
    def __init__(self, 
                 weight: float, 
                 radius: float, 
                 direction: List[float], 
                 coordinates: List[float], 
                 id: int):
        self.weight = weight
        self.radius = radius 
        self.direction = direction
        self.coordinates = coordinates
        self.id = id

