import unittest
from Utility import saveTree
from ConvertSortedArrayToBinarySearchTree import Solution

class Test(unittest.TestCase):


    def testSortedArrayToBST(self):
        s = Solution()
        nums = [[1, 2, 2, 3, 3, 4, 4], range(1, 9)]
        ans = [[3, 2, 4, 1, 2, 3, 4], [5, 3, 7, 2, 4, 6, 8, 1]]
        for num, an in zip(nums, ans):
            self.assertEqual(saveTree(s.sortedArrayToBST(num)), an, "result not agree")

if __name__ == "__main__":
    unittest.main()