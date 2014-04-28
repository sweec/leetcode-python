class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        l = len(num)
        for i in range(l-2, -1, -1):
            if num[i] < num[i+1]:
                index = l-1
                for j in range(i+2, l):
                    if num[j] <= num[i]:
                        index = j-1
                        break
                t = num[i]
                num[i] = num[index]
                num[index] = t
                a, b = i+1, l-1
                while a < b:
                    t = num[a]
                    num[a] = num[b]
                    num[b] = t
                    a += 1
                    b -= 1
                return num
        num.reverse()
        return num