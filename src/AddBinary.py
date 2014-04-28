class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        s = []
        l1, l2 = len(a), len(b)
        l = l2
        if l1 < l2:
            l = l1
            t = a
            a = b
            b = t
        carry = 0
        for i in range(1, l+1):
            bit = int(a[-i])+int(b[-i])+carry
            if bit < 2:
                carry = 0
            else:
                bit -= 2
                carry = 1
            s.append(str(bit))
        index = abs(l1-l2)-1
        while index >=0 and carry:
            bit = int(a[index])+carry
            if bit < 2:
                carry = 0
            else:
                bit -= 2
                carry = 1
            s.append(str(bit))
            index -= 1
        s.append(a[:index+1])
        if carry:
            s.append('1')
        s.reverse()
        return ''.join(s)