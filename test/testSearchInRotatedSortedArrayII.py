import unittest
from SearchInRotatedSortedArrayII import Solution

class Test(unittest.TestCase):


    def testSearch(self):
        s = Solution()
        A = [4,5,6,1,2,3]
        targets = [1, 5, 2, 7, 0, 6]
        ans = [True, True, True, False, False, True]
        for target, an in zip(targets, ans):
            self.assertEqual(s.search(A, target), an)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()