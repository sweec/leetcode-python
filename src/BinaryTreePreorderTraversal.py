class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        pt = []
        if not root:
            return pt
        stack = [root]
        while stack:
            r = stack.pop()
            pt.append(r.val)
            if r.right:
                stack.append(r.right)
            if r.left:
                stack.append(r.left)
        return pt
