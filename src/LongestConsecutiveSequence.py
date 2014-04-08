class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        lcs = 0
        pair = {}
        for n in num:
            if pair.get(n) is not None:
                continue
            v1 = pair.get(n-1)
            v2 = pair.get(n+1)
            low, high = n, n
            if v1 is not None and v1 < n:
                low = v1
                del pair[n-1]
            if v2 is not None and v2 > n:
                high = v2
                del pair[n+1]
            pair[low] = high
            pair[high] = low
            lcs = max(lcs, high-low+1)
        return lcs