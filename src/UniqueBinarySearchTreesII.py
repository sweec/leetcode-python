from Utility import TreeNode

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        if n < 1:
            return [None]
        if n == 1:
            node = TreeNode(1)
            return [node]
        A = self.generateTrees(n-1)
        for i in range(len(A)):
            cur, j = A[i], 0
            while cur:
                node = self.copy(A[i])
                A.append(node)
                k = 0
                while k < j:
                    node = node.right
                    k += 1
                newNode = TreeNode(node.val)
                newNode.left = node.left
                newNode.right = node.right
                node.val = n
                node.left = newNode
                node.right = None
                cur = cur.right
                j += 1
            node = A[i]
            while node.right:
                node = node.right
            node.right = TreeNode(n)
        return A 
    
    def copy(self, root):
        node = TreeNode(root.val)
        if root.left:
            node.left = self.copy(root.left)
        if root.right:
            node.right = self.copy(root.right)
        return node