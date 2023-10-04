from body import Body
from decimal import *

# constants
G = Decimal((0, (6, 6, 7, 4, 3, 0), -16)) 


class PhysicalLaws:
    """
    provides a state recalculation function for class Body and
    definition of some physical constants
    """

    def __init__(self):
        getcontext().prec = 80
        pass

    def GetNormSquared(self, first_coordinates, second_coordinates):
        norm_squared = Decimal(0)
        for i in range(len(first_coordinates)):
            norm_squared += ((first_coordinates[i] - second_coordinates[i]) ** 2)
        return norm_squared

    def RongeKuttaMethodHelper(self, m, h, v_t, norm_coeff, norm_squared):

        f = lambda r: (G * m / (r ** 2)) * norm_coeff
        g = lambda v: v
        

        q0 = f(norm_squared.sqrt())
        q1 = f(norm_squared.sqrt() + q0 / 2)
        q2 = f(norm_squared.sqrt() + q1 / 2)
        q3 = f(norm_squared.sqrt() + q2)

        k0 = g(v_t)
        k1 = g(v_t + k0 / 2)
        k2 = g(v_t + k1 / 2)
        k3 = g(v_t + k2)


        v_t_dt = v_t + h * (q0 + 2 * q1 + 2 * q2 + q3) / 6

        r_dt = h * (k0 + 2 * k1 + 2 * k2 + k3) / 6 #(v_t + v_t_dt) / 2
        return [r_dt, v_t_dt - v_t]


    def RongeKuttaMethod(self, first_body, second_body, accuracy):
        result_coord = []
        result_velocity = []
        m = second_body.weight;
        h = accuracy
        norm_squared = self.GetNormSquared(first_body.coordinates, second_body.coordinates)

        for i in range(len(first_body.coordinates)):
            distance = second_body.coordinates[i] - first_body.coordinates[i]
            norm_coeff = distance / norm_squared.sqrt()

            v_t = first_body.velocity[i]

            pre_result = self.RongeKuttaMethodHelper(m, h, v_t, norm_coeff, norm_squared)

            result_coord.append(pre_result[0])
            result_velocity.append(pre_result[1])

        return [result_coord, result_velocity]
        


    def EilerMethod(self, first_body, second_body, accuracy, time):
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
        return self.RongeKuttaMethod(first_body, second_body, accuracy)

    def Transformation(self, first_body: Body, second_body: Body, accuracy : Decimal, time: Decimal):
        result = self.TransformationShift(first_body, second_body, accuracy, time)

        return result

    def GetPotential(self, first, second) -> Decimal:
        return G * first.weight * second.weight / ((first[0] - second[0])**2 + (first[1] - second[1]) ** 2).sqrt()

    def GetKinetic(self, body) -> Decimal:
        return body.weight * (body.velocity[0]**2 + body.velocity[1]**2) / Decimal('2.0')
