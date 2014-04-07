class Solution:
    # @return an integer
    def maxArea(self, height):
        a, b = 0, len(height)-1
        most = 0
        while a < b:
            if not height[a]:
                a += 1
            elif not height[b]:
                b -= 1
            elif height[a] < height[b]:
                most = max(most, height[a]*(b-a))
                pre = height[a]
                while a < b and height[a] <= pre:
                    a += 1
            else:
                most = max(most, height[b]*(b-a))
                pre = height[b]
                while a < b and height[b] <= pre:
                    b -= 1
        return most