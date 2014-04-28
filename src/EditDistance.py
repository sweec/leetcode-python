class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        if word1 == word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        dists = [range(len(word2)+1)]
        for i in range(1, len(word1)+1):
            dists.append([i])
        for i, c1 in enumerate(word1):
            d = dists[i+1]
            for j, c2 in enumerate(word2):
                if c1 == c2:
                    d.append(dists[i][j])
                else:
                    d.append(min(min(dists[i][j], dists[i][j+1]), d[-1])+1)
        return dists[len(word1)][len(word2)]