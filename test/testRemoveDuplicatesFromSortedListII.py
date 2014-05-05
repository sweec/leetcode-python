import unittest
from Utility import getList, saveList
from RemoveDuplicatesFromSortedListII import Solution

class Test(unittest.TestCase):


    def testDeleteDuplicates(self):
        s = Solution()
        heads = [getList([1,2,3,3,4,4,5]), getList([1,1,1,2,3])]
        ans = [[1,2,5], [2,3]]
        for head,an in zip(heads, ans):
            self.assertEqual(saveList(s.deleteDuplicates(head)), an)

if __name__ == "__main__":
    unittest.main()