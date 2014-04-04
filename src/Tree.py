class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def getTree(A):
    if not A:
        return None
    head = TreeNode(A[0])
    curLayer = [head]
    i, size = 1, len(A)
    while i < size and curLayer:
        nextLayer = []
        for cur in curLayer:
            if i < size:
                if A[i] != '#':
                    left = TreeNode(A[i])
                    cur.left = left
                    nextLayer.append(left)
                i += 1
            else:
                break
            if i < size:
                if A[i] != '#':
                    right = TreeNode(A[i])
                    cur.right = right
                    nextLayer.append(right)
                i += 1
            else:
                break
        curLayer = nextLayer
    return head