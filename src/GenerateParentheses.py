class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        if not n:
            return ['']
        A = self.generateParenthesis(n-1)
        for i in range(len(A)):
            j = len(A[i])-1
            while j > 0 and A[i][j] == ')':
                A.append(''.join([A[i][:j], '(', A[i][j:], ')']))
                j -= 1
            A[i] = ''.join([A[i], '()'])
        return A