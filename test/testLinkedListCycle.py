import unittest
from LinkedListCycle import ListNode, Solution

class Test(unittest.TestCase):


    def testSingleNumber(self):
        s = Solution()
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        self.assertEqual(s.hasCycle(head), False, "result not agree")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()