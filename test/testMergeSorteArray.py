import unittest
from MergeSortedArray import Solution

class Test(unittest.TestCase):


    def testMerge(self):
        s = Solution()
        A = [1, 1, 2, 3, 3, 0, 0, 0]
        B = [1, 2, 3]
        an = [1, 1, 1, 2, 2, 3, 3, 3]
        s.merge(A, 5, B, 3)
        self.assertEqual(A, an)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()