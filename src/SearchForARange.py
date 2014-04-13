class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        if not A:
            return [-1, -1]
        return self.search(A, 0, len(A)-1, target)
    
    def search(self, A, start, end, target):
        if A[start]>target or A[end]<target:
            return [-1, -1]
        if A[start] == target and A[end] == target:
            return [start, end]
        m = start+(end-start)/2
        l = self.search(A, start, m, target)
        r = self.search(A, m+1, end, target)
        if l == [-1, -1] and r == [-1, -1]:
            return [-1, -1]
        if l == [-1, -1]:
            return r
        if r == [-1, -1]:
            return l
        return [l[0], r[1]]