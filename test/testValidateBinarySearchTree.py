import unittest
from Utility import getTree
from ValidateBinarySearchTree import Solution

class Test(unittest.TestCase):


    def testIsValidBST(self):
        s = Solution()
        root = getTree([1,'#',2,3])
        self.assertFalse(s.isValidBST(root))
        root = getTree([1,'#',2,'#',3])
        self.assertTrue(s.isValidBST(root))

if __name__ == "__main__":
    unittest.main()