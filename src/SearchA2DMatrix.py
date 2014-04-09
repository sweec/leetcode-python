class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        if m < 1:
            return False
        n = len(matrix[0])
        if n < 1:
            return False
        if matrix[0][0] > target or matrix[m-1][n-1] < target:
            return False
        if matrix[0][0] == target or matrix[m-1][n-1] == target:
            return True
        a, b = 0, m*n-1
        while a < b:
            mid = (a+b)/2
            if mid == a:
                return False
            x = mid/n
            y = mid - x*n
            if matrix[x][y] == target:
                return True
            if matrix[x][y] < target:
                a = mid
            else:
                b = mid