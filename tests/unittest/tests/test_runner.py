import unittest
import calculator_test

calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest((unittest.makeSuite(calculator_test.CalculatorTest)))
# calcTestSuite.addTest((unittest.makeSuite(...)))
print("count of tests:" + str(calcTestSuite.countTestCases()) + "\n")

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)