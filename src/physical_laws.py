import object

class PhysicalLaws:
    """
    this class provides a state recalculation function for class Object and
    definition of some physics constants
    """
    def __init__(self):
        """
        definition of recalculation function, G constant and etc
        """
        self.transformation = None
        self.G = 123 

    def TransformationShift(self, first_object : object.Object, second_object : object.Object):
        """
        the return value is how much the object should be changed
        """
        return None
