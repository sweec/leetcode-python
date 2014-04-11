import unittest
from Utility import getList, saveList
from RemoveNthNodeFromEndOfList import Solution

class Test(unittest.TestCase):


    def testRemoveNthFromEnd(self):
        s = Solution()
        head = getList([1,2,3,4,5])
        self.assertEqual(saveList(s.removeNthFromEnd(head, 1)), [1,2,3,4])

if __name__ == "__main__":
    unittest.main()