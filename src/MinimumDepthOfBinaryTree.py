class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        l, r = 0x7FFFFFFF, 0x7FFFFFFF
        if root.left:
            l = self.minDepth(root.left)
        if root.right:
            r = self.minDepth(root.right)
        return min(l,r)+1