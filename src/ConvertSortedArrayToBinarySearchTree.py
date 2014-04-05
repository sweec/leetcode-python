from Utility import TreeNode

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if not num:
            return None
        return self.sortedArrayToBSTHelper(num, 0, len(num))
    
    def sortedArrayToBSTHelper(self, num, start, end):
        index = start + (end - start)/2
        root = TreeNode(num[index])
        if index > start:
            root.left = self.sortedArrayToBSTHelper(num, start, index)
        if end > index+1:
            root.right = self.sortedArrayToBSTHelper(num, index+1, end)
        return root