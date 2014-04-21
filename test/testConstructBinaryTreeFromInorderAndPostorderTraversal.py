import unittest
from Utility import saveTree
from ConstructBinaryTreeFromInorderAndPostorderTraversal import Solution

class Test(unittest.TestCase):


    def testBuildTree(self):
        s = Solution()
        inorder = [1,2,3,4]
        postorder = [2,4,3,1]
        an = [1, '#', 3, 2, 4]
        self.assertEqual(saveTree(s.buildTree(inorder, postorder)), an)

if __name__ == "__main__":
    unittest.main()