import unittest
from BinaryTreeInorderTraversal import TreeNode, Solution

class Test(unittest.TestCase):


    def testInorderTraversal(self):
        s = Solution()
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        an = [1, 3, 2]
        pt = s.inorderTraversal(root)
        self.assertEqual(pt, an, "result not agree")

if __name__ == "__main__":
    unittest.main()