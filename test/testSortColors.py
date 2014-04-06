import unittest
from SortColors import Solution

class Test(unittest.TestCase):


    def testSortColors(self):
        s = Solution()
        A = [1, 2, 1, 2, 0, 0]
        an = [0, 0, 1, 1, 2, 2]
        s.sortColors(A)
        self.assertEqual(A, an)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()