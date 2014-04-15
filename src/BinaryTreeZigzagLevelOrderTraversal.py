class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        A = []
        curRow = [root]
        forward = True
        while curRow:
            vals = []
            nextRow = []
            for node in reversed(curRow):
                vals.append(node.val)
                if forward and node.left:
                    nextRow.append(node.left)
                if node.right:
                    nextRow.append(node.right)
                if not forward and node.left:
                    nextRow.append(node.left)
            A.append(vals)
            curRow = nextRow
            forward = not forward
        return A