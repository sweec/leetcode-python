class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        y, z = 0, x
        while x > 0:
            t = x/10
            y = y*10 + (x - t*10)
            x = t
        return y==z