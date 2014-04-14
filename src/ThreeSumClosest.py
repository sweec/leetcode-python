class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        N = len(num)
        if N < 4:
            return sum(num)
        num.sort()
        s1 = num[0]+num[1]+num[2]
        if s1 >= target:
            return s1
        s2 = num[N-3]+num[N-2]+num[N-1]
        if s2 <= target:
            return s2
        s, d = s1, target-s1
        if s2-target < d:
            s = s2
            d = s2 - target
        for i in range(N-2):
            if num[i]+num[i+1]+num[i+2]-target > d:
                break
            if target-(num[i]+num[N-2]+num[N-1]) > d:
                continue
            for j in range(i+1, N-1):
                s1 = num[i] + num[j] + num[j+1]
                d1 = s1-target
                if d1 == 0:
                    return s1
                elif d1 > 0:
                    if d1 < d:
                        s = s1
                        d = d1
                    break
                s2 = num[i] + num[j] + num[N-1]
                d2 = target - s2
                if d2 == 0:
                    return s2
                elif d2 > 0:
                    if d2 < d:
                        s = s2
                        d = d2
                    continue
                l, r, t = j+1, N-1, target-num[i]-num[j]
                while l < r:
                    m = l + (r-l)/2
                    if m == l:
                        break
                    if num[m] == t:
                        return target
                    if num[m] < t:
                        l = m
                    else:
                        r = m
                d1, d2 = t-num[l], num[r]-t
                if d1 < d:
                    s = target - d1
                    d = d1
                if d2 < d:
                    s = target + d2
                    d = d2
        return s