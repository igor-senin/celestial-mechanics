from body import Body
from decimal import *

from math import sqrt


# constants
G = Decimal((0, (6, 6, 7, 4, 3, 0), -16)) 


class PhysicalLaws:
    """
    provides a state recalculation function for class Body and
    definition of some physical constants
    """

    def __init__(self):
        pass

    def CalculateLawOfUniversalGravitation(self, first_body, second_body, accuracy, time):
        """
        in this function, using the Euler method, the increase in speed and the change 
        in the coordinates of one body relative to another are calculated according to 
        the law of universal gravitation
        """
        x_distance = second_body.coordinates[0] - first_body.coordinates[0]
        v_x = first_body.velocity[0]

        y_distance = second_body.coordinates[1] - first_body.coordinates[1]
        v_y = first_body.velocity[1]

        distance_squared = x_distance ** 2 + y_distance ** 2

        v_x_dt = v_x + accuracy * G * second_body.weight / distance_squared * (x_distance / distance_squared.sqrt())
        v_y_dt = v_y + accuracy * G * second_body.weight / distance_squared * (y_distance / distance_squared.sqrt())

        coordinates_shift = [(v_x_dt + v_x) / 2 * time, (v_y_dt + v_y) / 2 * time]
        velocity_shift =  [v_x_dt - v_x, v_y_dt - v_y]
        
        return [coordinates_shift, velocity_shift]



    def TransformationShift(self, first_body, second_body, accuracy, time):
        return self.CalculateLawOfUniversalGravitation(first_body, second_body, accuracy, time)

    def Transformation(self, first_body: Body, second_body: Body, accuracy : Decimal, time: Decimal):
        result = self.TransformationShift(first_body, second_body, accuracy, time)

        return result

    def GetPotential(self, first, second) -> Decimal:
        return G * first.weight * second.weight / ((first[0] - second[0])**2 + (first[1] - second[1]) ** 2).sqrt()

    def GetKinetic(self, body) -> Decimal:
        return body.weight * (body.velocity[0]**2 + body.velocity[1]**2) / Decimal('2.0')
