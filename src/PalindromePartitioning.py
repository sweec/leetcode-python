class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        parlindromes = []
        for i in range(len(s)):
            A = []
            for j in range(i, len(s)):
                A.append(self.isParlindrome(s, i, j))
            parlindromes.append(A)
        return self.partitionHelper(s, len(s), parlindromes)
    
    def partitionHelper(self, s, end, parlindromes):
        if not end:
            return []
        if end == 1:
            return [[s[0]]]
        A = []
        if parlindromes[0][end-1]:
            A = [[s[:end]]]
        for i in range(1, end):
            if parlindromes[i][end-1-i]:
                B = self.partitionHelper(s, i, parlindromes)
                for p in B:
                    p.append(s[i:end])
                    A.append(p)
        return A
    
    def isParlindrome(self, s, i, j):
        while j > i:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True