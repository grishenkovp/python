import unittest
import test_calc

calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest((unittest.makeSuite(test_calc.CalcBasicTest)))
calcTestSuite.addTest((unittest.makeSuite(test_calc.CalcExTest)))
print("count of tests:" + str(calcTestSuite.countTestCases()) + "\n")

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)
