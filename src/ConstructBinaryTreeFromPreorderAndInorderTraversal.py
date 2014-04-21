from Utility import TreeNode

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        return self.build(preorder, 0, len(preorder), inorder, 0, len(inorder))
    
    def build(self, preorder, s1, e1, inorder, s2, e2):
        size = e1 - s1
        if size <= 0:
            return None
        node = TreeNode(preorder[s1])
        if size == 1:
            return node
        if preorder[s1] == inorder[s2]:
            cur = node
            i = 1
            while (s1+i) < e1:
                if preorder[s1+i] != inorder[s2+i]:
                    break
                cur.right = TreeNode(preorder[s1+i])
                cur = cur.right
                i += 1
            if (s1+i) < e1:
                cur.right = self.build(preorder, s1+i, e1, inorder, s2+i, e2)
            return node
        if preorder[s1] == inorder[e2-1]:
            cur = node
            i = 1
            while (s1+i) < e1:
                if preorder[s1+i] != inorder[e2-1-i]:
                    break
                cur.left = TreeNode(preorder[s1+i])
                cur = cur.left
                i += 1
            if (s1+i) < e1:
                cur.left = self.build(preorder, s1+i, e1, inorder, s2, e2-i)
            return node
        i = s2 + 1
        while i < e2-1:
            if preorder[s1] == inorder[i]:
                break
            i += 1
        node.left = self.build(preorder, s1+1, s1+1+i-s2, inorder, s2, i)
        node.right = self.build(preorder, s1+1+i-s2, e1, inorder, i+1, e2)
        return node