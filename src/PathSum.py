class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right:
            if sum:
                return False
            return True
        if root.left and self.hasPathSum(root.left, sum):
            return True
        if root.right and self.hasPathSum(root.right, sum):
            return True
        return False