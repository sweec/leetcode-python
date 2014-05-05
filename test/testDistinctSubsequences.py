import unittest
from DistinctSubsequences import Solution

class Test(unittest.TestCase):


    def testNumDistinct(self):
        s = Solution()
        S = "rabbbit"
        T = "rabbit"
        self.assertEqual(s.numDistinct(S, T), 3)

if __name__ == "__main__":
    unittest.main()