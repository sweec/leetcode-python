class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort(reverse=True)
        return self.combination(candidates, 0, target)
    
    def combination(self, candidates, start, target):
        if target == 0:
            return [[]]
        end = len(candidates)
        if start >= end:
            return []
        val = candidates[start]
        start += 1
        while start<end and candidates[start] == val:
            start += 1
        A = self.combination(candidates, start, target)
        total = val
        for i in range(1, target/val+1):
            C = self.combination(candidates, start, target-total)
            for c in C:
                for _ in range(i):
                    c.append(val)
                A.append(c)
            total += val
        return A