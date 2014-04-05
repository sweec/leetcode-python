class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return self.getHeight(root) is not None
    
    def getHeight(self, root):
        if not root:
            return 0
        lh = self.getHeight(root.left)
        if lh is None:
            return None
        rh = self.getHeight(root.right)
        if rh is None:
            return None
        if abs(lh-rh) > 1:
            return None
        else:
            return max(lh,rh)+1