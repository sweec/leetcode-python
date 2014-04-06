import unittest
from NQueensII import Solution

class Test(unittest.TestCase):


    def testTotalNQueens(self):
        s = Solution()
        ns = [1, 2, 3, 4];
        ans = [1, 0, 0, 2];
        for n, an in zip(ns, ans):
            num = s.totalNQueens(n)
            self.assertEqual(num, an)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()