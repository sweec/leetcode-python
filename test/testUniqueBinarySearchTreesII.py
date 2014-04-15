import unittest
from Utility import saveTree
from UniqueBinarySearchTreesII import Solution

class Test(unittest.TestCase):


    def testGenerateTrees(self):
        s = Solution()
        an = [[1,'#',2,'#',3],[2,1,3],[3,1,'#','#',2],[1,'#',3,2],[3,2,'#',1]]
        A = [saveTree(root) for root in s.generateTrees(3)]
        self.assertEqual(A, an)

if __name__ == "__main__":
    unittest.main()