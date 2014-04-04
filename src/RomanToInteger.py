class Solution:
    # @return an integer
    def romanToInt(self, s):
        num = 0
        for d in reversed(s):
            pre = num
            if num < 11:
                if d == 'I':
                    if num < 5:
                        num += 1
                    else:
                        num -= 1
                elif d == 'V':
                    num += 5
            if pre != num:
                continue
            if num < 110:
                if d == 'X':
                    if num < 50:
                        num += 10
                    else:
                        num -= 10
                elif d == 'L':
                    num += 50
            if pre != num:
                continue
            if d == 'C':
                if num < 500:
                    num += 100
                else:
                    num -= 100
            elif d == 'D':
                num += 500
            else:
                num += 1000
        return num                