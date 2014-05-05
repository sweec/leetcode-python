from Utility import ListNode

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        fh = ListNode(0)
        fh.next = head
        pre, cur = fh, head
        while cur:
            after = cur.next
            while after and after.val == cur.val:
                after = after.next
            if after == cur.next:
                pre = cur
            else:
                pre.next = after
            cur = after
        return fh.next