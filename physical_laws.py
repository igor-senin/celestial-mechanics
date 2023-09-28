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
        """
        in this function, using the Euler method, the increase in speed and the change 
        in the coordinates of one body relative to another are calculated according to 
        the law of universal gravitation
        """
        x_distance = second_body.coordinates[0] - first_body.coordinates[0]
        v_x = second_body.velocity[0]

        y_distance = second_body.coordinates[1] - first_body.coordinates[1]
        v_y = second_body.velocity[1]

        distance_squared = x_distance ** 2 + y_distance ** 2

        v_x_dt = v_x + accuracy * -self.G * second_body.weight / distance_squared * (-1 if x_distance < 0 else 1)
        v_y_dt = v_y + accuracy * -self.G * second_body.weight / distance_squared * (-1 if y_distance < 0 else 1)

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

    def GetPotential(self, first, second) -> float:
        return self.G * first.weight * second.weight / sqrt((first[0] -
                                                             second[0])**2 +
                                                            (first[1] -
                                                             second[1]) ** 2)

    def GetKinetic(self, body) -> float:
        return body.weight * (body.velocity[0]**2 + body.velocity[1]**2) / 2.0
