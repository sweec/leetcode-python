class Solution:
    board, ans, limit = None, None, 0
    # @return a list of lists of string
    def solveNQueens(self, n):
        self.board = [['.' for _ in range(n)] for _ in range(n)]
        self.ans = []
        self.limit = (1<<n) - 1
        self.dfs(0, 0, 0, 0)
        return self.ans
        
    def dfs(self, h, r, l, row):
        if h == self.limit:
            A = []
            for line in self.board:
                A.append(''.join(line))
            self.ans.append(A)
            return
        pos = self.limit & (~(h|r|l))
        index = -1
        while pos:
            p = pos & (-pos)    #return most right bit 1
            pos -= p
            for i in range(index+1, 32):
                if p == 1<<i:
                    index = i
                    break
            self.board[row][index] = 'Q'
            self.dfs(h+p, (r+p)<<1, (l+p)>>1, row+1)   #no shift needed for h, left shift for anti diagonal
            self.board[row][index] = '.'