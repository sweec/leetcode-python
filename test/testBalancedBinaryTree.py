import unittest
from Utility import getTree
from BalancedBinaryTree import Solution

class Test(unittest.TestCase):


    def testIsBalanced(self):
        s = Solution()
        p = getTree([1, 2, 2, 3, 4, 4, 3])
        self.assertEqual(s.isBalanced(p), True, "result not agree")
        q = getTree([1, 2, 2, '#', 3, '#', '#', 4])
        self.assertEqual(s.isBalanced(q), False, "result not agree")

if __name__ == "__main__":
    unittest.main()