class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        first = root
        while True:
            pre = first
            while pre and (not pre.left) and (not pre.right):
                pre = pre.next
            if not pre:
                break;
            cur = None
            if pre.left:
                cur = pre.left
            else:
                cur = pre.right
            first = cur
            if (cur == pre.left) and pre.right:
                cur.next = pre.right
                cur = cur.next
            while pre.next:
                pre = pre.next
                if pre.left:
                    cur.next = pre.left
                    cur = cur.next
                if pre.right:
                    cur.next = pre.right
                    cur = cur.next
        