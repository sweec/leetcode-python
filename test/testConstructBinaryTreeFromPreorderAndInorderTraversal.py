import unittest
from Utility import saveTree
from ConstructBinaryTreeFromPreorderAndInorderTraversal import Solution

class Test(unittest.TestCase):


    def testBuildTree(self):
        s = Solution()
        inorder = [1,2,3,4]
        preorder = [1,3,2,4]
        an = [1, '#', 3, 2, 4]
        self.assertEqual(saveTree(s.buildTree(preorder, inorder)), an)

if __name__ == "__main__":
    unittest.main()