class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        if n < k or k == 0:
            return []
        if n == k:
            return [range(1, n+1)]
        if k == 1:
            return [[i] for i in range(1, n+1)]
        A = self.combine(n-1, k)
        for c in self.combine(n-1, k-1):
            c.append(n)
            A.append(c)
        return A