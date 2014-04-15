import unittest
from Triangle import Solution

class Test(unittest.TestCase):


    def testMinimumTotal(self):
        s = Solution()
        triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
        self.assertEqual(s.minimumTotal(triangle), 11)

if __name__ == "__main__":
    unittest.main()