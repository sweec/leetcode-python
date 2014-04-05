import unittest
from RemoveDuplicatesFromSortedArray import Solution

class Test(unittest.TestCase):


    def testRemoveDuplicates(self):
        s = Solution()
        A = [1, 1, 2, 2, 3, 3]
        num = s.removeDuplicates(A)
        self.assertEqual(num, 3, "single number is wrong")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()