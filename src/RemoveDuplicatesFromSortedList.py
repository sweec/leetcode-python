class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        node = head
        while node:
            nextNode = node.next
            while nextNode and nextNode.val == node.val:
                nextNode = nextNode.next
            node.next = nextNode
            node = nextNode
        return head