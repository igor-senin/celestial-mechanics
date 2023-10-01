import body
import physical_laws
from decimal import *

from typing import List


class System:
    """
        Class of the system we will module, can be set accuracy for 
    recalculation transformation, centre of system wich we will 
    module and physical laws.
        We can add bodies to the sytem and recalculate system using
    corresponding function
    """

    def __init__(self, physical_laws, bodies):
        self.bodies = bodies 
        self.accuracy = Decimal('0.03')
        self.time = self.accuracy # may be unused
        self.physical_laws = physical_laws
        self.UsePreCoordinates = False

        bodies_copy = self.bodies.copy()
        bodies_size = len(bodies_copy)

        for i in range(bodies_size):
            for j in range(bodies_size):
                if i == j:
                    continue
                i_data = self.physical_laws.EilerMethod(bodies_copy[i], bodies_copy[j], self.accuracy / 2, self.time / 2)

                for k in range(len(i_data[0])):
                    print(i, k, i_data[0][k])
                    print(i, k, i_data[1][k])
                    self.bodies[i].pre_coordinates[k] += i_data[0][k]
                    self.bodies[i].pre_velocity[k] += i_data[1][k]
                  
        print()
        for i in range(bodies_size):
            for k in range(len(self.bodies[i].coordinates)):
                print("    coord ", self.bodies[i].coordinates[k])
                print("pre_coord ", self.bodies[i].pre_coordinates[k])
                print("    coordc", bodies_copy[i].coordinates[k])
                print("pre_coordc", bodies_copy[i].pre_coordinates[k])

                print("    veloc ", self.bodies[i].velocity[k])
                print("pre_veloc ", self.bodies[i].pre_velocity[k])
                print("    velocc", bodies_copy[i].velocity[k])
                print("pre_velocc", bodies_copy[i].pre_velocity[k])


    def AddBody(self, body):
        self.bodies.append(body)

    def RecalculateSystem(self):
        bodies_copy = self.bodies.copy()
        bodies_size = len(bodies_copy)

        potential = Decimal(0)
        kinetic = Decimal(0)

        for i in range(bodies_size):
            for j in range(bodies_size):
                if i == j:
                    continue

                potential += self.physical_laws.GetPotential(bodies_copy[i], bodies_copy[j])
                kinetic += self.physical_laws.GetKinetic(bodies_copy[i])

                i_data = self.physical_laws.Transformation(bodies_copy[i], bodies_copy[j], self.accuracy, self.time, self.UsePreCoordinates)

                for k in range(len(i_data[0])):
                    if (self.UsePreCoordinates == False):
                        self.bodies[i].coordinates[k] += i_data[0][k]
                        self.bodies[i].velocity[k] += i_data[1][k]
                    else:
                        self.bodies[i].pre_coordinates[k] += i_data[0][k]
                        self.bodies[i].pre_velocity[k] += i_data[1][k]

        self.UsePreCoordinates =  False if self.UsePreCoordinates else True


#        print(f"total potential energy: {potential}")
#        print(f"total kinetic energy: {kinetic}")
#        print(f"sum: {kinetic+potential}")
#        print("\n\n\n")


    def GetCoordinates(self, index):
        return self.bodies[index].coordinates

    def GetID(self, index):
        return self.bodies[index].id

    def GetBodies(self):
        return self.bodies

    def GetWeightCenter(self) -> List[Decimal]:
        weight_sum = Decimal('0.0')
        for b in self.bodies:
            weight_sum += b.weight
        center = [Decimal('0.0'), Decimal('0.0')]
        for b in self.bodies:
            center[0] += (b.weight / weight_sum) * b[0]
            center[1] += (b.weight / weight_sum) * b[1]
        return center
