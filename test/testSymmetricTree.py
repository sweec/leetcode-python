import unittest
from Utility import getTree
from SymmetricTree import Solution

class Test(unittest.TestCase):


    def testIsSymmetric(self):
        s = Solution()
        p = getTree([1, 2, 2, 3, 4, 4, 3])
        self.assertEqual(s.isSymmetric(p), True, "result not agree")
        q = getTree([1, 2, 2, '#', 3, '#', 3])
        self.assertEqual(s.isSymmetric(q), False, "result not agree")

if __name__ == "__main__":
    unittest.main()