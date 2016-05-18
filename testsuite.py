import unittest

from test_cases import testcase, testcase_2, testcase_3, testcase_4, testcase_5

def suite():
    test_suite = unittest.TestSuite()

    # Test cases to execute
    test_suite.addTest(testcase.suite())
    """"
    test_suite.addTest(testcase_2.suite())
    test_suite.addTest(testcase_3.suite())
    test_suite.addTest(testcase_4.suite())
    test_suite.addTest(testcase_5.suite())
    """
    return test_suite

if __name__ == "__main__":
    #So you can run tests from this package individually.
    log_file = 'log_file.txt'
    f = open(log_file, "w")
    TEST_RUNNER = unittest.TextTestRunner(f,verbosity=2)
    TEST_SUITE = suite()
    TEST_RUNNER.run(TEST_SUITE)
    f.close()
