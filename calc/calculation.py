""" This is our base class : Calculation """
# This is an abstract class
# This is where we create our objects


class Calculation:
    """ This is the Calculation class """

    def __init__(self, values: tuple):
        """ This is the Calculation constructor """
        self.values = Calculation.convert_vals_to_list(values)

    # Class Factory Method
    @staticmethod
    def convert_vals_to_list(values):
        """ This converts values to a list of floats """
        float_list = []
        for item in values:
            if isinstance(item,str):
                float_list.append("nan")
            else:
                float_list.append(float(item))
        return float_list
