import unittest
from SearchA2DMatrix import Solution

class Test(unittest.TestCase):


    def testSearchMatrix(self):
        s = Solution()
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
        ts = [3, 15]
        ans = [True, False]
        for target, an in zip(ts, ans):
            self.assertEqual(s.searchMatrix(matrix, target), an)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()