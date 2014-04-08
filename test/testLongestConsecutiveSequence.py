import unittest
from LongestConsecutiveSequence import Solution

class Test(unittest.TestCase):


    def testLongestConsecutive(self):
        s = Solution()
        A = [100, 4, 200, 1, 3, 2]
        self.assertEqual(s.longestConsecutive(A), 4)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()