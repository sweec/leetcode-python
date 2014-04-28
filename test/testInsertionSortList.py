import unittest
from Utility import getList, saveList
from InsertionSortList import Solution

class Test(unittest.TestCase):


    def testInsertionSortList(self):
        s = Solution()
        head = getList([0, 1, 3, 2, 6, 7, 5, 4])
        an = range(8)
        self.assertEqual(saveList(s.insertionSortList(head)), an)

if __name__ == "__main__":
    unittest.main()