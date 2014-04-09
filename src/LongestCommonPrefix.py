class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        n = 0x7FFFFFFF
        for s in strs:
            n = min(n, len(s))
        if n==0x7FFFFFFF or n==0:
            return ''
        for i in range(n):
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
        return strs[0][:n]