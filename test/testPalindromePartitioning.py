import unittest
from PalindromePartitioning import Solution

class Test(unittest.TestCase):


    def testPartition(self):
        s = Solution()
        S = "aab"
        an = [["aa","b"],["a","a","b"]]
        A = s.partition(S)
        self.assertEqual(len(A), len(an))
        for p in A:
            self.assertTrue(p in an)

if __name__ == "__main__":
    unittest.main()