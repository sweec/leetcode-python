class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        l, r = 0, len(A)-1
        while l <= r:
            if A[l] == target or A[r] == target:
                return True
            m = l + (r-l)/2
            if m == l:
                return False
            if A[m] == target:
                return True
            if A[l] < A[m]:
                if A[l] < target and target < A[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif A[m] < A[r]:
                if A[m] < target and target < A[r]:
                    l = m + 1
                else:
                    r = m - 1
            elif A[l] > A[r]:
                if A[l] == A[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                l += 1
                r -= 1
        return False