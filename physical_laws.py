from body import Body
from util import Vector

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

    # TODO: Lists -> Vector
    def RongeKuttaMethod(self, first_body, second_body, h, use_pre):
        norm_squared = Decimal(0)
        result = [[], []]
        m = second_body.weight;
        if use_pre == False:
            for i in range(len(first_body.coordinates)):
                norm_squared += (first_body.coordinates[i] - second_body.coordinates[i]) ** 2

            for i in range(len(first_body.coordinates)):
                distance = second_body.coordinates[i] - first_body.coordinates[i]
                norm_coeff = distance / norm_squared.sqrt()

                r_t = first_body.coordinates[i]
                r_t_dt2 = first_body.pre_coordinates[i]
                v_t = first_body.velocity[i]

                k0 = v_t
                q0 = G * m / r_t ** 2 * norm_coeff 
                k1 = v_t + q0 * h / 2
                q1 = G * m / (r_t_dt2 + k0 * h / 2) * norm_coeff 
                k2 = v_t + q1 * h / 2
                q2 = G * m / (r_t_dt2  + k1 * h / 2)
                k3 = v_t + q2 * h 
                q3 = G * m / (r_t + k2 * h)
                v_t_dt = v_t + h / 6 * (q0 + 2 * q1 + 2 * q2 + q3)
                r_t_dt = r_t + h / 6 * (k0 + 2 * k1 + 2 * k2 + k3)
                result[0].append(r_t_dt - r_t)
                result[1].append(v_t_dt - v_t)
        else:
            for i in range(len(first_body.pre_coordinates)):
                norm_squared += (first_body.pre_coordinates[i] - second_body.pre_coordinates[i]) ** 2

            for i in range(len(first_body.pre_coordinates)):
                distance = second_body.pre_coordinates[i] - first_body.pre_coordinates[i]
                norm_coeff = distance / norm_squared.sqrt()

                r_t = first_body.pre_coordinates[i]
                r_t_dt2 = first_body.coordinates[i]
                v_t = first_body.pre_velocity[i]

                k0 = v_t
                q0 = G * m / r_t ** 2 * norm_coeff 
                k1 = v_t + q0 * h / 2
                q1 = G * m / (r_t_dt2 + k0 * h / 2) * norm_coeff 
                k2 = v_t + q1 * h / 2
                q2 = G * m / (r_t_dt2  + k1 * h / 2)
                k3 = v_t + q2 * h 
                q3 = G * m / (r_t + k2 * h)
                v_t_dt = v_t + h / 6 * (q0 + 2 * q1 + 2 * q2 + q3)
                r_t_dt = r_t + h / 6 * (k0 + 2 * k1 + 2 * k2 + k3)
                result[0].append(r_t_dt - r_t)
                result[1].append(v_t_dt - v_t)

        return result
        


    def EulerMethod(self, first_body, second_body, accuracy, time):
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



    def TransformationShift(self, first_body, second_body, accuracy, time, use_pre):
        return self.RongeKuttaMethod(first_body, second_body, accuracy, use_pre)

    def Transformation(self, first_body: Body, second_body: Body, accuracy : Decimal, time: Decimal, use_pre : bool):
        result = self.TransformationShift(first_body, second_body, accuracy, time, use_pre)

        return result

    def GetPotential(self, first, second) -> Decimal:
        return G * first.weight * second.weight / ((first[0] - second[0])**2 + (first[1] - second[1]) ** 2).sqrt()

    def GetKinetic(self, body) -> Decimal:
        return body.weight * (body.velocity[0]**2 + body.velocity[1]**2) / Decimal('2.0')
