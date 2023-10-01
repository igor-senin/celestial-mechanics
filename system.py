import body
import physical_laws


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
        self.accuracy = 10**(-4)
        self.time = self.accuracy # may be unused
        self.physical_laws = physical_laws

    def AddBody(self, body):
        self.bodies.append(body)

    def RecalculateSystem(self):
        bodies_copy = self.bodies.copy()
        bodies_size = len(bodies_copy)

        potential = 0
        kinetic = 0

        for i in range(bodies_size):
            for j in range(bodies_size):
                if i == j:
                    continue

                #if bodies_copy[i].id == 1:
                #    continue

                potential += self.physical_laws.GetPotential(bodies_copy[i], bodies_copy[j])
                kinetic += self.physical_laws.GetKinetic(bodies_copy[i])

                #print(i, j)
                i_data = self.physical_laws.Transformation(bodies_copy[i], bodies_copy[j], self.accuracy, self.time)
                #i_data = self.physical_laws.Transformation(bodies_copy[j], bodies_copy[i], self.accuracy, self.time)
                for k in range(len(i_data[0])):
                    #print(j_data[0][k], j_data[1][k],)
                    self.bodies[i].coordinates[k] += i_data[0][k]
                    self.bodies[i].velocity[k] += i_data[1][k]
                    #self.bodies[i].coordinates[k] -= i_data[0][k]
                    #self.bodies[i].velocity[k] -= i_data[1][k]

        print(f"total potential energy: {potential}")
        print(f"total kinetic energy: {kinetic}")
        print(f"sum: {kinetic+potential}")
        print("\n\n\n")


    def GetCoordinates(self, index):
        return self.bodies[index].coordinates

    def GetID(self, index):
        return self.bodies[index].id

    def GetBodies(self):
        return self.bodies

