import unittest
from Permutations import Solution

class Test(unittest.TestCase):


    def testPermute(self):
        s = Solution()
        A = [1, 2, 3]
        an = [[3, 1, 2], [2, 3, 1], [2, 1, 3], [3, 2, 1], [1, 3, 2], [1, 2, 3]]
        self.assertEqual(s.permute(A), an)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()