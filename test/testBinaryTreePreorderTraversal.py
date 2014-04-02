import unittest
from BinaryTreePreorderTraversal import TreeNode, Solution

class Test(unittest.TestCase):


    def testSameTree(self):
        s = Solution()
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        an = [1, 2, 3]
        pt = s.preorderTraversal(root)
        self.assertEqual(pt, an, "result not agree")

if __name__ == "__main__":
    unittest.main()