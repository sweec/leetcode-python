class Solution:
    # @return a list of integers
    def grayCode(self, n):
        A = [0]
        for i in xrange(n):
            bit = 1 << i
            for j in xrange(len(A)-1, -1, -1):
                A.append(bit+A[j])
        return A