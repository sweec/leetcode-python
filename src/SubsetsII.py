class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        A = [[]]
        pre, preCount = None, 1
        S.sort()
        for n in S:
            count = len(A)
            if n == pre:
                count = preCount
            else:
                pre = n
                preCount = count
            for i in range(len(A)-count, len(A)):
                ss = A[i][:]
                ss.append(n)
                A.append(ss)
        return A