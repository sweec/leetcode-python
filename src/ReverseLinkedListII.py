from Utility import ListNode

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if m == n:
            return head
        fh = ListNode(0)
        fh.next = head
        pre, cur = fh, head
        count = 1
        while count < m:
            pre = cur
            cur = cur.next
            count += 1
        t, h = cur, cur
        cur = cur.next
        while count < n:
            after = cur.next
            cur.next = h
            h = cur
            cur = after
            count += 1
        pre.next = h
        t.next = cur
        return fh.next