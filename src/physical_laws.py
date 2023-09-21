import object
import math

class PhysicalLaws:
    """
    provides a state recalculation function for class Object and
    definition of some physics constants
    """
    def __init__(self):
        """
        definition of recalculation function, G constant and etc
        """
        self.G = 6.67430e11 

    def CalculateLawOfUniversalGravitation(self, first_object, second_object, time):
        x_distance = second_object.coordinate[0] - first_object.coordinate[0]
        y_distance = second_object.coordinate[1] - first_object.coordinate[1]
        distance_squared = x_distance ** 2 + y_distance ** 2

        a = self.G * second_object.weight / distance_squared
        
        x_distance_normalized = x_distance / math.sqrt(distance_squared)
        y_distance_normalized = y_distance / math.sqrt(distance_squared)

        coordinate_shift = [x_distance_normalized * a * time ** 2, y_distance_normalized * a * time ** 2]
        direction_shift = [x_distance_normalized * a * time, y_distance_normalized * a * time]
        return [coordinate_shift, direction_shift]



    def TransformationShift(self, first_object, second_object, time):
        return self.CalculateLawOfUniversalGravitation(first_object, second_object, time)


        

    def Transformation(self, first_object : object.Object, second_object : object.Object, time : float):
        """
        the return value is how much the object should be changed
        """
        result = self.TransformationShift(first_object, second_object, time)

        new_x_coordinate = result[0][0] + second_object.coordinate[0]
        new_y_coordinate = result[0][1] + second_object.coordinate[1]

        return [[new_x_coordinate, new_y_coordinate], 
                 result[1][0], result[1][1]]
