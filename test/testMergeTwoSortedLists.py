import unittest
from MergeTwoSortedLists import ListNode, Solution

class Test(unittest.TestCase):


    def testMergeTwoLists(self):
        s = Solution()
        l1 = ListNode(1)
        l1.next = ListNode(3)
        l1.next.next = ListNode(5)
        l2 = ListNode(2)
        l2.next = ListNode(4)
        l2.next.next = ListNode(6)
        head = s.mergeTwoLists(l1, l2)
        ans = range(1, 7)
        cur = head
        for an in ans:
            self.assertEqual(cur.val, an, "result not agree")
            cur = cur.next

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()