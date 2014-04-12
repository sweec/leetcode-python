import unittest
from UniquePathsII import Solution

class Test(unittest.TestCase):


    def testNumTrees(self):
        s = Solution()
        obstacleGrid = [[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]]
        an = 7
        self.assertEqual(s.uniquePathsWithObstacles(obstacleGrid), an)

if __name__ == "__main__":
    unittest.main()