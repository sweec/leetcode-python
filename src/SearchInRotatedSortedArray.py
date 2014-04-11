class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return an integer
    def search(self, A, target):
        l, r = 0, len(A)-1
        while l <= r:
            if A[l] == target:
                return l
            if A[r] == target:
                return r
            m = l + (r-l)/2
            if m == l:
                return -1
            if A[m] == target:
                return m
            if A[l] < A[m]:
                if A[l] < target and target < A[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if A[m] < target and target < A[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1