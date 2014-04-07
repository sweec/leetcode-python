import unittest
from MinimumPathSum import Solution

class Test(unittest.TestCase):


    def testMinPathSum(self):
        s = Solution()
        grid = [[1,3,1],[1,5,1],[4,2,1]]
        self.assertEqual(s.minPathSum(grid), 7)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()