from Utility import ListNode

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if k < 2:
            return head
        fh = ListNode(0)
        fh.next = head
        pre, cur = fh, head
        while cur:
            count = 1
            while cur.next and count<k:
                count += 1
                cur = cur.next
            if count < k:
                break
            before = pre.next
            pre.next = cur
            pre = before
            after = before.next
            pre.next = cur.next
            while before != cur:
                t = after.next
                after.next = before
                before = after
                after = t
            cur = pre.next
        return fh.next