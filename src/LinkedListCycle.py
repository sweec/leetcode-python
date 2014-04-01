class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head is None:
            return False
        fast = head
        slow = head
        while True:
            if fast.next is None:
                return False
            if fast.next is slow:
                return True
            fast = fast.next
            if fast.next is None:
                return False
            if fast.next is slow:
                return True
            fast = fast.next
            slow = slow.next