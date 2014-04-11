class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        eindex = rain = block = 0 # eindex is expected-bar-index, which is last highest.
        for i in range(1, len(A)):
            if A[i] >= A[eindex]:
                rain += (i-eindex-1)*A[eindex] - block
                block = 0
                eindex = i
            else:
                block += A[i]

        highest = eindex
        block = 0
        eindex = len(A)-1
        for i in range(len(A)-2, highest-1, -1):
            if A[i] > A[eindex]:
                rain += (eindex-i-1)*A[eindex] - block
                block = 0
                eindex = i
            else:
                block += A[i]
        return rain