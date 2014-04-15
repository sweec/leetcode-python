import unittest
from Utility import getList, saveList
from PartitionList import Solution

class Test(unittest.TestCase):


    def testPartition(self):
        s = Solution()
        head = getList([1,4,3,2,5,2])
        an = [1,2,2,4,3,5]
        self.assertEqual(saveList(s.partition(head, 3)), an)

if __name__ == "__main__":
    unittest.main()