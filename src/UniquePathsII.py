class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        curLayer = [1]
        for i in range(m+n-1):
            if i < n:
                x, y = 0, i
            else:
                x, y = i-n+1, n-1
            nextLayer = []
            cango = False
            j = 0
            while x < m and y >= 0:
                pre = curLayer[0]
                if obstacleGrid[x][y]:
                    pre = 0
                else:
                    if not x and y:
                        pre = curLayer[j]
                    elif x and not y:
                        pre = curLayer[-1]
                    elif x and y:
                        pre = curLayer[j]+curLayer[j+1]
                if pre:
                    cango = True
                nextLayer.append(pre)
                if x and y:
                    j += 1
                x += 1
                y -= 1
            if not cango:
                return 0
            curLayer = nextLayer
        return curLayer[0]