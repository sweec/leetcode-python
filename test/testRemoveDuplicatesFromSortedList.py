import unittest
from RemoveDuplicatesFromSortedList import ListNode, Solution

class Test(unittest.TestCase):


    def testSingleNumber(self):
        s = Solution()
        head = ListNode(1)
        head.next = ListNode(1)
        head.next.next = ListNode(2)
        head.next.next.next = ListNode(3)
        head.next.next.next.next = ListNode(3)
        head = s.deleteDuplicates(head)
        self.assertIsNotNone(head)
        self.assertEqual(head.val, 1, "result not agree")
        self.assertIsNotNone(head.next)
        self.assertEqual(head.next.val, 2, "result not agree")
        self.assertIsNotNone(head.next.next)
        self.assertEqual(head.next.next.val, 3, "result not agree")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()