class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 0:
            return 1
        if x == 0:
            if n >= 0:
                return 0
            else:
                return None
        if n < 0:
            x = 1/x
            n = -n
        negative = False
        if x<0 and (n&1):
            negative = True
        x = abs(x)
        p, cur, i = 1.0, x, 0
        while n:
            if n&(1<<i):
                p *= cur
                n ^= 1<<i
            cur *= cur
            i += 1
        if negative:
            p = -p
        return p