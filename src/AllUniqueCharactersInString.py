class Solution():
    # @param A, a string (ASCII characters only)
    # @return a boolean
    def isAllUnique(self, A):
        count = 0
        for c in A:
            if count & (1 << ord(c)):
                return False
            count |= 1 << ord(c)
        return True