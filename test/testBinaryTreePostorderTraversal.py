import unittest
from BinaryTreePostorderTraversal import TreeNode, Solution

class Test(unittest.TestCase):


    def testPostorderTraversal(self):
        s = Solution()
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        an = [3, 2, 1]
        pt = s.postorderTraversal(root)
        self.assertEqual(pt, an, "result not agree")

if __name__ == "__main__":
    unittest.main()