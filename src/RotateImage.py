class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        x = -1
        for i in range(n-1, 0, -2):
            x += 1
            y = x
            for j in range(i):
                t = matrix[x][y+j]
                matrix[x][y+j] = matrix[x+i-j][y]
                matrix[x+i-j][y] = matrix[x+i][y+i-j]
                matrix[x+i][y+i-j] = matrix[x+j][y+i]
                matrix[x+j][y+i] = t
        return matrix