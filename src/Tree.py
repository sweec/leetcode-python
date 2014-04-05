class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def getTree(A):
    if not A:
        return None
    root = TreeNode(A[0])
    curLayer = [root]
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
    return root

def saveTree(root):
    if not root:
        return []
    curLayer = [root]
    A = [root.val]
    while curLayer:
        nextLayer = []
        for cur in curLayer:
            if cur.left:
                A.append(cur.left.val)
                nextLayer.append(cur.left)
            else:
                A.append('#')
            if cur.right:
                A.append(cur.right.val)
                nextLayer.append(cur.right)
            else:
                A.append('#')
        curLayer = nextLayer
    last = A.pop()
    while last == '#':
        last = A.pop()
    A.append(last)
    return A