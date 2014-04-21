from Utility import TreeNode

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        return self.build(inorder, 0, len(inorder), postorder, 0, len(postorder))
    
    def build(self, inorder, s1, e1, postorder, s2, e2):
        size = e1 - s1
        if size <= 0:
            return None
        node = TreeNode(inorder[s1])
        if size == 1:
            return node
        if inorder[s1] == postorder[s2]:
            i = 1
            while (s1+i) < e1:
                if inorder[s1+i] != postorder[s2+i]:
                    break
                cur = TreeNode(inorder[s1+i])
                cur.left = node
                node = cur
                i += 1
            if (s1+i) < e1:
                root = self.build(inorder, s1+i, e1, postorder, s2+i, e2)
                cur = root
                while cur.left:
                    cur = cur.left
                cur.left = node
                node = root
            return node
        if inorder[s1] == postorder[e2-1]:
            cur = node
            i = 1
            while (s1+i) < e1:
                if inorder[s1+i] != postorder[e2-1-i]:
                    break
                cur.right = TreeNode(inorder[s1+i])
                cur = cur.right
                i += 1
            if (s1+i) < e1:
                root = self.build(inorder, s1+i, e1, postorder, s2, e2-i)
                cur.right = root
            return node
        i = s2 + 1
        while i < e2-1:
            if postorder[i] == inorder[s1]:
                break
            i += 1
        right = self.build(inorder, s1+1, s1+1+i-s2, postorder, s2, i)
        node.right = right
        root = self.build(inorder, s1+1+i-s2, e1, postorder, i+1, e2)
        cur = root
        while cur.left:
            cur = cur.left
        cur.left = node
        return root