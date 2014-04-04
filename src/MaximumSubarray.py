class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        val = -0x80000000
        s = 0
        for n in A:
            if val <= 0:
                val = max(val, n)
                if n > 0:
                    s = n
            elif s > 0 or n > 0:
                s += n;
                if n > 0:
                    val = max(val, s)
                elif s < 0:
                    s = 0
        return val