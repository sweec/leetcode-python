class Solution:
    strs = [[''],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z'],[' ']]
    
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        return self.letter(digits, len(digits))
    
    def letter(self, digits, end):
        if not end:
            return ['']
        A = self.letter(digits, end-1)
        index = int(digits[end-1])-1
        for i in range(len(A)):
            for j in range(1, len(self.strs[index])):
                A.append(''.join([A[i], self.strs[index][j]]))
            A[i] = ''.join([A[i], self.strs[index][0]])
        return A