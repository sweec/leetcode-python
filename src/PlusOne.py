class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        c, i = 1, len(digits)-1
        while c and i>=0:
            digits[i] += c
            if digits[i] == 10:
                digits[i] = 0
                i -= 1
            else:
                c = 0
        if c:
            digits.insert(0, c)
        return digits