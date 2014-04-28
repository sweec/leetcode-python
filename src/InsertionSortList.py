from Utility import ListNode

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head:
            return head
        fh = ListNode(0)
        fh.next = head
        cur = head
        while cur.next:
            if cur.next.val < cur.val:
                pre = fh
                while pre.next.val < cur.next.val:
                    pre = pre.next
                t = cur.next
                cur.next = t.next
                t.next = pre.next
                pre.next = t
            else:
                cur = cur.next
        return fh.next