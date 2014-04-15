from Utility import ListNode
class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        l, r = ListNode(0), head
        prel, l.next = l, head
        while r and r.val < x:
            prel = r
            r = r.next
        if not r:
            return head
        prer, cur = r, r.next
        while cur:
            if cur.val < x:
                prer.next = cur.next
                prel.next = cur
                prel = cur
                cur = prer.next
            else:
                prer = cur
                cur = cur.next
        prel.next = r
        return l.next