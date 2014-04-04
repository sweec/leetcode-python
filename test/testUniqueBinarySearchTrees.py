import unittest
from UniqueBinarySearchTrees import Solution

class Test(unittest.TestCase):


    def testNumTrees(self):
        s = Solution()
        ns = [1, 2, 3, 4]
        ans = [1, 2, 5, 14]
        for n, an in zip(ns, ans):
            num = s.numTrees(n)
            self.assertEqual(num, an, "Unique tree number not agree")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()