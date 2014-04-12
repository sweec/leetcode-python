class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        num = [0 for _ in range(9)]
        for i, row in enumerate(board):
            for j, n in enumerate(row):
                if n != '.':
                    n = int(n)
                    if num[i] & (1<<n):
                        return False
                    else:
                        num[i] |= 1<<n
                    if num[j] & (1<<(n+9)):
                        return False
                    else:
                        num[j] |= (1<<(n+9))
                    k = (i/3)*3+(j/3)
                    if num[k] & (1<<(n+18)):
                        return False
                    else:
                        num[k] |= (1<<(n+18))
        return True