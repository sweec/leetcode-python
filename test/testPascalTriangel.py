import unittest
from PascalTriangle import Solution

class Test(unittest.TestCase):


    def testGenerate(self):
        s = Solution()
        an = [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
        A = s.generate(5)
        self.assertEqual(A, an, "Triangle not agree")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()