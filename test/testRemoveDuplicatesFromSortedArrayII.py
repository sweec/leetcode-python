import unittest
from RemoveDuplicatesFromSortedArrayII import Solution

class Test(unittest.TestCase):


    def testRemoveDuplicates(self):
        s = Solution()
        A = [1, 1, 1, 2, 2, 3, ]
        self.assertEqual(s.removeDuplicates(A), 5)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()