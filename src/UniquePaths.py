class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        s, k = m+n-2, min(m, n)-1
        num = 1
        for i in range(1, k+1):
            num = num * (s-k+i) / i
        return num