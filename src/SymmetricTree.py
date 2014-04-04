class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root:
            return True
        stack = [[root.left, root.right]]
        while stack:
            node = stack.pop()
            left, right = node[0], node[1]
            if left and right:
                if left.val != right.val:
                    return False
                stack.append([left.left, right.right])
                stack.append([left.right, right.left])
            elif not (not left and not right):
                return False
        return True