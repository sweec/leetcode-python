import unittest
from MaximumDepthOfBinaryTree import TreeNode, Solution

class Test(unittest.TestCase):


    def testSameTree(self):
        s = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        self.assertEqual(s.maxDepth(root), 3, "result not agree")

if __name__ == "__main__":
    unittest.main()