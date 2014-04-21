import unittest
from Utility import getList, saveList
from ReverseLinkedListII import Solution

class Test(unittest.TestCase):


    def testReverseBetween(self):
        s = Solution()
        head = getList([0, 1, 3, 2, 6, 7, 5, 4])
        an = [0, 6, 2, 3, 1, 7, 5, 4]
        self.assertEqual(saveList(s.reverseBetween(head, 2, 5)), an)

if __name__ == "__main__":
    unittest.main()