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
        for i in range(len(objects_copy)):
            for j in range(len(objects_copy)):
                if i != j:
                    self.objects[i] += self.physical_laws.TransformationShift(objects_copy[i], objects_copy[j])
                    self.objects[j] += self.physical_laws.TransformationShift(objects_copy[j], objects_copy[i])

    def GetCoordinates(self, index):
        return self.objects[index].coordinate

    def GetID(self, index):
        return self.objects[index].id

