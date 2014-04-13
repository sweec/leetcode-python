class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if not root:
            return
        pre = None
        stack = [root]
        while stack:
            r = stack.pop()
            if pre:
                pre.left = None
                pre.right = r
            pre = r
            if r.right:
                stack.append(r.right)
            if r.left:
                stack.append(r.left)