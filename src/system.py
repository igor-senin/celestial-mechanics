import object
import physical_laws

class System:

    """
        Class of the system we will module, can be set accuracy for 
    recalculation transformation, centre of system wich we will 
    module and physical laws.
        We can add objects to the sytem and recalculate system using
    corresponding function

    """

    def __init__(self, accuracy, centre, physical_laws : physical_laws.PhysicalLaws):
        self.objects = list()
        self.accuracy = accuracy
        self.centre = centre
        self.physical_laws = physical_laws

    def AddObject(self, object : object.Object):
        self.objects.append(object)

    def RecalculateSystem(self):
        objects_copy = self.objects
        objects_size = len(objects_copy)

        for i in range(objects_size):
            for j in range(len(self.objects[i].coordinate)):
                self.objects[i].coordinate[j] /= objects_size

        for i in range(objects_size):
            for j in range(objects_size):
                if i != j:
                    j_data = self.physical_laws.Transformation(objects_copy[i], objects_copy[j], self.accuracy)
                    i_data = self.physical_laws.Transformation(objects_copy[j], objects_copy[i], self.accuracy)
                    for k in range(len(j_data[0])):
                        j_data[0][k] /= objects_size
                        i_data[0][k] /= objects_size
                        self.objects[j].coordinate[k] += j_data[0][k]
                        self.objects[i].coordinate[k] += i_data[0][k]
                        self.objects[j].direction[k] += j_data[1][k]
                        self.objects[i].direction[k] += i_data[1][k]


    def GetCoordinates(self, index):
        return self.objects[index].coordinate

    def GetID(self, index):
        return self.objects[index].id

