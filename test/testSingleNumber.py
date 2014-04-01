import unittest
from SingleNumber import Solution

class Test(unittest.TestCase):


    def testSingleNumber(self):
        s = Solution()
        A = [1, 1, 2, 3, 3]
        num = s.singleNumber(A)
        self.assertEqual(num, 2, "single number is wrong")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()