import unittest
from Utility import getTree
from BinaryTreeLevelOrderTraversalII import Solution

class Test(unittest.TestCase):


    def testIsSymmetric(self):
        s = Solution()
        p = getTree([1, 2, 2, 3, 4, 4, 3])
        an = [[3, 4, 4, 3], [2, 2], [1]]
        self.assertEqual(s.levelOrderBottom(p), an)
        q = getTree([1, 2, 2, '#', 3, '#', 3])
        an = [[3, 3], [2, 2], [1]]
        self.assertEqual(s.levelOrderBottom(q), an)

if __name__ == "__main__":
    unittest.main()