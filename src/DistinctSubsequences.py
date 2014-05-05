class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        m, n = len(S), len(T)
        if m < n:
            return 0
        count = [1 for _ in range(m+1)]
        for j in range(n):
            for i in range(m-j):
                num = 0
                if i > 0:
                    num = count[i-1]
                if S[j+i] == T[j]:
                    num += count[i]
                count[i] = num
        return count[m-n]