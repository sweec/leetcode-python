import unittest
from Utility import getList, saveTree
from ConvertSortedListToBinarySearchTree import Solution

class Test(unittest.TestCase):


    def testGrayCode(self):
        s = Solution()
        head = getList(range(5))
        an = [2, 1, 4, 0, '#', 3]
        self.assertEqual(saveTree(s.sortedListToBST(head)), an)

if __name__ == "__main__":
    unittest.main()