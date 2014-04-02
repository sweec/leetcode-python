class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
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
                stack.append([r, True])
                if r.right:
                    stack.append([r.right, False])
                if r.left:
                    stack.append([r.left, False])
        return pt