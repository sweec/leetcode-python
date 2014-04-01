class Solution:
    # @return an integer
    def reverse(self, x):
        maxint = 0x7FFFFFFF
        if x == 0:
            return 0
        neg = False
        if x < 0:
            neg = True
            x = -x
        r = 0
        while x > 0:
            y = x / 10
            n = x - y*10
            x = y
            r = r*10 + n
            if (not neg) and (r >= maxint):
                r = maxint
                break
            if neg and r > maxint:
                r = maxint + 1
                break
        if neg:
            r = -r
        return r