class Solution:
    # @return a boolean
    def isValid(self, s):
        A = []
        size = len(s)
        for i, c in enumerate(s):
            j = ')}]'.find(c)
            if j >= 0:
                if not A or A.pop() != '({['[j]:
                    return False
            else:
                A.append(c)
            if len(A) > (size-i-1):
                return False
        return True