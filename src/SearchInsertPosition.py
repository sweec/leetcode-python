class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if not A or target <= A[0]:
            return 0
        size = len(A)
        if target > A[size-1]:
            return size
        if target == A[size-1]:
            return size-1
        i = 0
        j = size-1
        while True:
            m = (i+j)/2
            if target == A[m]:
                return m
            if m == i:
                return m+1
            if target > A[m]:
                i = m
            else:
                j = m