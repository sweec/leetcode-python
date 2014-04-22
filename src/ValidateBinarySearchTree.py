class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        if not root:
            return True
        return self.validBST(root, -0x80000001, 0x80000000)
    
    def validBST(self, root, minValue, maxValue):
        if root.val <= minValue or root.val >= maxValue:
            return False
        if root.left and not self.validBST(root.left, minValue, root.val):
            return False
        if root.right and not self.validBST(root.right, root.val, maxValue):
            return False
        return True