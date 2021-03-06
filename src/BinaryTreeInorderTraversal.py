class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        pt = []
        if not root:
            return pt
        stack = [[root, False]]
        while stack:
            node = stack.pop()
            r = node[0]
            if node[1]:
                pt.append(r.val)
            else:
                if r.right:
                    stack.append([r.right, False])
                stack.append([r, True])
                if r.left:
                    stack.append([r.left, False])
        return pt