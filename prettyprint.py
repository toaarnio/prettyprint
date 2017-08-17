#!/usr/bin/python -B

from pprint import PrettyPrinter

def pprint(object, stream=None, indent=1, width=80, depth=None, decimals=4):
    """Equivalent of pprint.pprint() with fixed-width decimal printing."""
    printer = _FixedDecimalPrettyPrinter(stream=stream, indent=indent, width=width, depth=depth)
    printer._floatFormatStr = "%%.%df"%(decimals)
    printer.pprint(object)

def pformat(object, stream=None, indent=1, width=80, depth=None, decimals=4):
    """Equivalent of pprint.pformat() with fixed-width decimal printing."""
    printer = _FixedDecimalPrettyPrinter(stream=stream, indent=indent, width=width, depth=depth)
    printer._floatFormatStr = "%%.%df"%(decimals)
    return printer.pformat(object)

class _FixedDecimalPrettyPrinter(PrettyPrinter):
    def format(self, theObject, context, maxlevels, level):
        if isinstance(theObject, float):
            return self._floatFormatStr%(theObject), True, False
        else:
            return PrettyPrinter.format(self, theObject, context, maxlevels, level)

######################################################################################
#
#  U N I T   T E S T S
#
######################################################################################

if __name__ == "__main__":

    import unittest

    class _TestPrettyPrinter(unittest.TestCase):
        def test_pformat(self):
            array = [3.1415926, 2.7198, 2.0, 1.3333]
            result = pformat(array, decimals=3)
            expected = "[3.142, 2.720, 2.000, 1.333]"  # note the rounding
            self.assertEqual(expected, result)

    suite = unittest.TestLoader().loadTestsFromTestCase(_TestPrettyPrinter)
    unittest.TextTestRunner(verbosity=0).run(suite)
