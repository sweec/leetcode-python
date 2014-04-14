class Solution:
    # @return a string
    def countAndSay(self, n):
        if n == 1:
            return '1'
        s1 = '1'
        for _ in range(1, n):
            s2 = []
            pre, count = s1[0], 1
            for j in range(1, len(s1)):
                if s1[j] == pre:
                    count += 1
                else:
                    s2.append(str(count))
                    s2.append(str(pre))
                    pre = s1[j]
                    count = 1
            s2.append(str(count))
            s2.append(str(pre))
            s1 = ''.join(s2)
        return s1