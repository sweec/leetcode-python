class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        if not num:
            return []
        num.sort()
        return self.permute(num, len(num))
    
    def permute(self, num, end):
        if num[0] == num[end-1]:
            return [num[:end]]
        A = self.permute(num, end-1)
        for i in range(len(A)):
            for j in range(len(A[i])-1, -1, -1):
                if A[i][j] == num[end-1]:
                    break
                else:
                    p = A[i][:]
                    p.insert(j, num[end-1])
                    A.append(p)
            A[i].append(num[end-1])
        return A