class Solution():
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if not head or not n:
            return head
        i, p, q = 0, head, head
        while p and i < n:
            p = p.next
            i += 1
        if i < n:
            return head
        if not p:
            return head.next
        while p.next:
            p = p.next
            q = q.next
        q.next = q.next.next
        return head