from typing import List

class Object:
    """
    presents Objects like Moon or Sun or other with their parametrs 
    like weight or speed
    """
    def __init__(self, 
                 weight : float, 
                 radius : float, 
                 direction : List[float], 
                 coordinate : List[float], 
                 id : int):
        self.weight = weight
        self.radius = radius 
        self.direction = direction
        self.coordinate = coordinate
        self.id = id

