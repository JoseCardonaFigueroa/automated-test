import unittest
from test_cases import testcase, testcase_2, testcase_3, testcase_4, testcase_5

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(testcase.suite())
    return test_suite

if __name__ == "__main__":
    #So you can run tests from this package individually.
    TEST_RUNNER = unittest.TextTestRunner()
    TEST_SUITE = suite()
    TEST_RUNNER.run(TEST_SUITE)
