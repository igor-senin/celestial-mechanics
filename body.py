from typing import List

class Body:
    """
    represents celestial bodies like Moon, Sun or other
    with their parameters like weight or speed
    """
    def __init__(self, 
                 weight: float, 
                 radius: float, 
                 coordinates: List[float], 
                 velocity: List[float],
                 id: int):
        self.weight = weight
        self.radius = radius 
        self.coordinates = coordinates
        self.velocity = velocity
        self.id = id

    def __getitem__(self, ind):
        return self.coordinates[ind]

