import unittest
from SearchInsertPosition import Solution

class Test(unittest.TestCase):


    def testSingleNumber(self):
        s = Solution()
        A = [1,3,5,6]
        targets = [1, 5, 2, 7, 0, 6]
        ans = [0, 2, 1, 4, 0, 3]
        for target, an in zip(targets, ans):
            self.assertEqual(s.searchInsert(A, target), an, "Insert position not agree")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()