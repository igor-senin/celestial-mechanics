from body import Body

from math import sqrt


class PhysicalLaws:
    """
    provides a state recalculation function for class Body and
    definition of some physical constants
    """
    G = 6.67430e11 

    def __init__(self):
        pass
    
    def CalculateLawOfUniversalGravitation(self, first_body, second_body, time):
        x_distance = second_body.coordinates[0] - first_body.coordinates[0]
        y_distance = second_body.coordinates[1] - first_body.coordinates[1]
        distance_squared = x_distance ** 2 + y_distance ** 2

        a = self.G * second_body.weight / distance_squared
        
        x_distance_normalized = x_distance / sqrt(distance_squared)
        y_distance_normalized = y_distance / sqrt(distance_squared)

        coordinate_shift = [
                x_distance_normalized * a * time ** 2,
                y_distance_normalized * a * time ** 2
                ]
        direction_shift = [
                x_distance_normalized * a * time,
                y_distance_normalized * a * time
                ]
        return [coordinate_shift, direction_shift]



    def TransformationShift(self, first_body, second_body, time):
        return self.CalculateLawOfUniversalGravitation(first_body, second_body, time)

    def Transformation(self, first_body: Body, second_body: Body, time: float):
        """
        the return value is list of coordinates and direction after update
        """
        result = self.TransformationShift(first_body, second_body, time)

        new_x_coordinate = result[0][0] + second_body.coordinate[0]
        new_y_coordinate = result[0][1] + second_body.coordinate[1]

        return [[new_x_coordinate, new_y_coordinate], 
                 result[1][0], result[1][1]]
