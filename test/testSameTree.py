import unittest
from SameTree import TreeNode, Solution

class Test(unittest.TestCase):


    def testSameTree(self):
        s = Solution()
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(4)
        self.assertEqual(s.isSameTree(p, q), False, "result not agree")

if __name__ == "__main__":
    unittest.main()