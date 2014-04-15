import unittest
from GrayCode import Solution

class Test(unittest.TestCase):


    def testGrayCode(self):
        s = Solution()
        an = [0, 1, 3, 2, 6, 7, 5, 4]
        A = s.grayCode(3)
        self.assertEqual(A, an)

if __name__ == "__main__":
    unittest.main()