class Object:
    """
    this class presents Objects like Moon or Sun or other with their parametrs 
    like weight or speed
    """
    def __init__(self, weight, radius, speed, direction, coordinate, id):
        self.weight = weight
        self.radius = radius 
        self.speed = speed 
        self.direction = direction
        self.coordinate = coordinate
        self.id = id

