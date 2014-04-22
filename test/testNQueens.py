import unittest
from NQueens import Solution

class Test(unittest.TestCase):


    def testSolveNQueens(self):
        s = Solution()
        ans = [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]];
        A = s.solveNQueens(4)
        self.assertEqual(len(A), len(ans))
        for an in A:
            self.assertTrue(an in ans)

if __name__ == "__main__":
    unittest.main()