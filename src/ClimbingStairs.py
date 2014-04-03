class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n < 1:
            return 0
        pre = 0
        cur = 1
        for i in range(1, n+1):
            cur = pre + cur
            pre = cur - pre
        return cur