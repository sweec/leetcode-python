import unittest
from PermutationsII import Solution

class Test(unittest.TestCase):


    def testPermuteUnique(self):
        s = Solution()
        num = [1, 1, 2]
        an = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        A = s.permuteUnique(num)
        self.assertEqual(len(A), len(an))
        for a in A:
            print(a)
            self.assertTrue(a in an)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()