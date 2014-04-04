import unittest
from RemoveElement import Solution

class Test(unittest.TestCase):


    def testRemoveElement(self):
        s = Solution()
        A = [1]
        num = s.removeElement(A, 1)
        self.assertEqual(num, 0, "new length is wrong")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()