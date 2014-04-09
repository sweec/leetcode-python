class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    # since python has unlimited precision for long type
    # simple version just
    # return str(long(num1)*long(num2))
    def multiply(self, num1, num2):
        result = [0]
        s1,s2 = len(num1),len(num2)
        for i in range((s1+3)/4):
            a = int(num1[max(0, s1-(i+1)*4):s1-i*4])
            if a:
                for j in range((s2+3)/4):
                    b = int(num2[max(0, s2-(j+1)*4):s2-j*4])
                    if b:
                        self.add(result, a*b, (i+j)*4)
        return ''.join([str(d) for d in reversed(result)])
    
    def add(self, result, val, numZero):
        s1 = len(result)
        valstr = str(val)
        if s1 <= numZero:
            for _ in range(numZero-s1):
                result.append(0)
            for c in reversed(valstr):
                result.append(int(c))
        else:
            s2 = numZero+len(valstr)
            low, high = min(s1, s2), max(s1, s2)
            carry = 0
            for i in range(numZero, high):
                s = carry
                if i < low:
                    s += result[i] + int(valstr[s2-i-1])
                elif i < s1:
                    s += result[i]
                else:
                    s += int(valstr[s2-i-1])
                if (s > 9):
                    s -= 10
                    carry = 1
                else:
                    carry = 0
                if i < s1:
                    result[i] = s
                    if i >= s2 and not carry:
                        break
                else:
                    result.append(s)
            if carry:
                result.append(1)