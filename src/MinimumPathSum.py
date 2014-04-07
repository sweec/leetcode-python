class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m = len(grid)
        if not m:
            return 0
        n = len(grid[0])
        if not n:
            return 0
        curLayer = []
        for i in range(m+n-1):
            if i < n:
                x, y = 0, i
            else:
                x, y = i-n+1, n-1
            nextLayer = []
            j = 0
            while x < m and y >= 0:
                pre = 0
                if not x and y:
                    pre = curLayer[j]
                elif x and not y:
                    pre = curLayer[-1]
                elif x and y:
                    pre = min(curLayer[j], curLayer[j+1])
                    j += 1
                nextLayer.append(pre+grid[x][y])
                x += 1
                y -= 1
            curLayer = nextLayer
        return curLayer[0]