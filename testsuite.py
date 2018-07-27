import unittest
from alltestcase import TestMultifunc
def suite_calc ():
	suite_calc = unittest.TestSuite()
	suite_calc.addTest(TestMultifunc('test_add_2positive_number'))
	suite_calc.addTest(TestMultifunc('test_fact'))
	suite_calc.addTest(TestMultifunc('test_fact_Invalidinput'))
	return suite_calc
	return suite_calc
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite_calc())

