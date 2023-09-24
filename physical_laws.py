from body import Body

from math import sqrt


class PhysicalLaws:
    """
    provides a state recalculation function for class Body and
    definition of some physical constants
    """
    G = 6.67430e-11 

    def __init__(self):
        pass
    
    def CalculateLawOfUniversalGravitation(self, first_body, second_body, accuracy, time):
        x_distance = second_body.coordinates[0] - first_body.coordinates[0]
        v_x = second_body.direction[0]

        y_distance = second_body.coordinates[1] - first_body.coordinates[1]
        v_y = second_body.direction[1]

        distance_squared = x_distance ** 2 + y_distance ** 2

        v_x_dt = v_x + accuracy * -self.G * second_body.weight / distance_squared
        v_y_dt = v_y + accuracy * -self.G * second_body.weight / distance_squared

        coordinate_shift = [v_x_dt  * time, v_y_dt * time]
        direction_shift =  [v_x_dt - v_x, v_y_dt - v_y]
        
        return [coordinate_shift, direction_shift]



    def TransformationShift(self, first_body, second_body, accuracy, time):
        return self.CalculateLawOfUniversalGravitation(first_body, second_body, accuracy, time)

    def Transformation(self, first_body: Body, second_body: Body, accuracy : float, time: float):
        """
        """
        result = self.TransformationShift(first_body, second_body, accuracy, time)

        return result
