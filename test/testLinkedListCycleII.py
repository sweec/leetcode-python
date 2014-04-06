import unittest
from Utility import getList
from LinkedListCycleII import Solution

class Test(unittest.TestCase):


    def testHasCycle(self):
        s = Solution()
        head = getList([1, 2, 3])
        head.next.next.next = head.next
        self.assertEqual(s.detectCycle(head), head.next)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()