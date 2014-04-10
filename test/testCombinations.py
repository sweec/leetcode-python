import unittest
from Combinations import Solution

class Test(unittest.TestCase):


    def testGrayCode(self):
        s = Solution()
        n, k = 4, 2
        an = [[2,4], [3,4], [2,3], [1,2], [1,3], [1,4]]
        A = s.combine(n, k)
        self.assertEqual(len(A), len(an))
        for a in A:
            self.assertTrue(a in an)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()