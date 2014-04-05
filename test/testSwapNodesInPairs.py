import unittest
from Utility import getList, saveList
from SwapNodesInPairs import Solution

class Test(unittest.TestCase):


    def testSwapPairs(self):
        s = Solution()
        head = getList([1, 2, 3])
        head = s.swapPairs(head)
        vals = saveList(head)
        an = [2, 1, 3]
        self.assertEqual(vals, an)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()