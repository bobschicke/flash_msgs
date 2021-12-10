""" This is the Addition Calculation """
# This class inherits value_a and value_b from Calculation class
# Namespace
from calc.calculation import Calculation

# Putting a Class in the parenthasis is how you extend a class
class Addition(Calculation):
    """ This is the addition class"""

    def get_result(self):
        """ This function does the calculation and returns the result """
        result = self.values.pop(0)
        #loop through values and do the Addition
        for items in self.values:
            if isinstance(items,str):
                return "nan"
            result += items
        return result
