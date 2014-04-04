class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        pre = head
        while l1 and l2:
            if l1.val <= l2.val:
                pre.next = l1
                while l1.next and l1.next.val <= l2.val:
                    l1 = l1.next
                pre = l1
                l1 = l1.next
            else:
                pre.next = l2
                while l2.next and l2.next.val <= l1.val:
                    l2 = l2.next
                pre = l2
                l2 = l2.next
        if l1:
            pre.next = l1
        else:
            pre.next = l2
        return head.next