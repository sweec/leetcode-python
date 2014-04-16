import unittest
from CombinationSum import Solution

class Test(unittest.TestCase):


    def testCombinationSum(self):
        s = Solution()
        candidates = [2,3,6,7]
        an = [[2,2,3], [7]]
        self.assertEqual(s.combinationSum(candidates, 7), an)

if __name__ == "__main__":
    unittest.main()