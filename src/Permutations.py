class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        return self.permuteHelper(num, len(num))
    
    def permuteHelper(self, num, end):
        if not end:
            return [[]]
        A = []
        pre = self.permuteHelper(num, end-1)
        for p in pre:
            p.append(num[end-1])
            for i in range(end-1):
                c = p[:]
                c[end-1] = c[i]
                c[i] = num[end-1]
                A.append(c)
            A.append(p)
        return A