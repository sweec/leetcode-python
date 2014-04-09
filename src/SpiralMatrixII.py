class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if not n:
            return []
        matrix = [[n*n for _ in range(n)] for _ in range(n)]
        num = 1
        for dim in range(n, 0, -2):
            num = self.generateMatrixHelper(matrix, num, dim, n)
        return matrix
    
    def generateMatrixHelper(self, matrix, num, dim, n):
        x = (n-dim)/2
        y = x
        for j in range(dim-1):
            matrix[x][y+j] = num
            num += 1
        for i in range(dim-1):
            matrix[x+i][y+dim-1] = num
            num += 1
        for j in reversed(range(1, dim)):
            matrix[x+dim-1][y+j] = num
            num += 1
        for i in reversed(range(1, dim)):
            matrix[x+i][y] = num
            num += 1
        return num