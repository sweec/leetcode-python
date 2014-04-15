import unittest
from Utility import getTree
from BinaryTreeZigzagLevelOrderTraversal import Solution

class Test(unittest.TestCase):


    def testZigzagLevelOrder(self):
        s = Solution()
        root = getTree([3,9,20,'#','#',15,7])
        an = [[3],[20,9],[15,7]]
        self.assertEqual(s.zigzagLevelOrder(root), an)

if __name__ == "__main__":
    unittest.main()