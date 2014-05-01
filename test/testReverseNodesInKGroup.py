import unittest
from Utility import getList, saveList
from ReverseNodesInKGroup import Solution

class Test(unittest.TestCase):


    def testReverseKGroup(self):
        s = Solution()
        heads = [getList(range(1,6)), getList(range(1,6))]
        ks = [2,3]
        ans = [[2,1,4,3,5], [3,2,1,4,5]]
        for head, k, an in zip(heads, ks, ans):
            self.assertEqual(saveList(s.reverseKGroup(head, k)), an)

if __name__ == "__main__":
    unittest.main()