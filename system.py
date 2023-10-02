import body
import physical_laws
from decimal import *
from util import Vector

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
        self.bodies = bodies # no copy
        self.accuracy = Decimal('0.03')
        self.time = self.accuracy # may be unused
        self.physical_laws = physical_laws
        self.UsePreCoordinates = False

        bodies_copy = self.bodies.copy()

        for i in range(len(bodies_copy)):
            for j in range(len(bodies_copy)):
                if i == j:
                    continue
                i_data = self.physical_laws.EulerMethod(bodies_copy[i], bodies_copy[j], self.accuracy / 2, self.time / 2)
                self.bodies[i].pre_coordinates += i_data[0]
                self.bodies[i].pre_velocity += i_data[1]

    def RecalculateSystem(self):
        bodies_copy = self.bodies.copy()

        potential = Decimal(0)
        kinetic = Decimal(0)

        for i in range(len(bodies_copy)):
            for j in range(len(bodies_copy)):
                if i == j:
                    continue

                potential += self.physical_laws.GetPotential(bodies_copy[i], bodies_copy[j])
                kinetic += self.physical_laws.GetKinetic(bodies_copy[i])

                i_data = self.physical_laws.Transformation(bodies_copy[i], bodies_copy[j], self.accuracy, self.time, self.UsePreCoordinates)

                if not self.UsePreCoordinates:
                    self.bodies[i].coordinates += i_data[0]
                    self.bodies[i].velocity += i_data[1]
                else:
                    self.bodies[i].pre_coordinates += i_data[0]
                    self.bodies[i].pre_velocity += i_data[1]

        self.UsePreCoordinates = not self.UsePreCoordinates


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

    def GetWeightCenter(self) -> Vector:
        weight_sum = Decimal('0.0')
        for b in self.bodies:
            weight_sum += b.weight
        center = Vector([Decimal('0.0'), Decimal('0.0')])
        for b in self.bodies:
            center += (b.weight / weight_sum) * b.coordinates
        return center
