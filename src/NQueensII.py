class Solution:
    ans, limit = 0, 0
    # @return an integer
    def totalNQueens(self, n):
        self.ans = 0
        self.limit = (1<<n) - 1
        self.dfs(0, 0, 0)
        return self.ans
        
    def dfs(self, h, r, l):
        if h == self.limit:
            self.ans += 1
            return
        pos = self.limit & (~(h|r|l))
        while pos:
            p = pos & (-pos)    #return most right bit 1
            pos -= p
            self.dfs(h+p, (r+p)<<1, (l+p)>>1)   #no shift needed for h, left shift for anti diagonal