class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        p1, p2 = head, head
        while p2 and p2.next:
            p2 = p2.next.next
            p1 = p1.next
            if p2 == p1:
                while head != p1:
                    head = head.next
                    p1 = p1.next
                return head