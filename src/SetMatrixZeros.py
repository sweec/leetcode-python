class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if not matrix or not matrix[0]:
            return
        row1Zero, col1Zero = False, False
        m, n = len(matrix), len(matrix[0])
        for num in matrix[0]:
            if num == 0:
                row1Zero = True
                break
        for i in range(m):
            if matrix[i][0] == 0:
                col1Zero = True
                break
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] and (matrix[i][0] == 0 or matrix[0][j] == 0):
                    matrix[i][j] = 0
        if row1Zero:
            for j in range(n):
                matrix[0][j] = 0
        if col1Zero:
            for i in range(m):
                matrix[i][0] = 0