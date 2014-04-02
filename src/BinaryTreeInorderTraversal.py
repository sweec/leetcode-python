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
            if (not r.left):
                pt.append(r.val)
                if r.right:
                    stack.append([r.right, False])
            elif node[1]:
                pt.append(r.val)
            else:
                if r.right:
                    stack.append([r.right, False])
                stack.append([r, True])
                stack.append([r.left, False])
        return pt