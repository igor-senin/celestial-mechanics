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

    def __init__(self, accuracy, centre, physical_laws, bodies):
        self.bodies = bodies 
        self.accuracy = accuracy
        self.time = accuracy # may be unused
        self.centre = centre
        self.physical_laws = physical_laws

    def AddBody(self, body):
        self.bodies.append(body)

    def RecalculateSystem(self):
        bodies_copy = self.bodies.copy()
        bodies_size = len(bodies_copy)

        for i in range(bodies_size):
            for j in range(bodies_size):
                if i == j:
                    continue

                print(i, j)
                j_data = self.physical_laws.Transformation(bodies_copy[i], bodies_copy[j], self.accuracy, self.time)
                #i_data = self.physical_laws.Transformation(bodies_copy[j], bodies_copy[i], self.accuracy, self.time)
                for k in range(len(j_data[0])):
                    print(j_data[0][k], j_data[1][k],)
                    self.bodies[j].coordinates[k] += j_data[0][k]
                    self.bodies[j].velocity[k] += j_data[1][k]
                    #self.bodies[i].coordinates[k] -= i_data[0][k]
                    #self.bodies[i].velocity[k] -= i_data[1][k]


    def GetCoordinates(self, index):
        return self.bodies[index].coordinates

    def GetID(self, index):
        return self.bodies[index].id

    def GetBodies(self):
        return self.bodies

