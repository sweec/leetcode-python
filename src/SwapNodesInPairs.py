from Utility import ListNode

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        pre = ListNode(0)
        pre.next = head
        cur = head
        head = pre
        while cur and cur.next:
            pre.next = cur.next
            cur.next = pre.next.next
            pre.next.next = cur
            pre = cur
            cur = cur.next
        return head.next