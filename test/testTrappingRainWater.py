import unittest
from TrappingRainWater import Solution

class Test(unittest.TestCase):


    def testTrap(self):
        s = Solution()
        A = [5,4,1,2]
        self.assertEqual(s.trap(A), 1)

if __name__ == "__main__":
    unittest.main()