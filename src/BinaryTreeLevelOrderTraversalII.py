class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if not root:
            return []
        A = []
        curLayer = [root]
        while curLayer:
            nextLayer = []
            vals = []
            for node in curLayer:
                vals.append(node.val)
                if node.left:
                    nextLayer.append(node.left)
                if node.right:
                    nextLayer.append(node.right)
            A.append(vals)
            curLayer = nextLayer
        A.reverse()
        return A