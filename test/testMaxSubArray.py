import unittest
from MaximumSubarray import Solution

class Test(unittest.TestCase):


    def testMaxSubArray(self):
        s = Solution()
        A = [-2,1,-3,4,-1,2,1,-5,4]
        num = s.maxSubArray(A)
        self.assertEqual(num, 6, "max is wrong")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()