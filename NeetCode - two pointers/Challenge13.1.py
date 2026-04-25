class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n
        i = 0
        j = n - 1

        maxL = 0
        maxR = 0

        while i < n:
            maxLeft[i] = maxL
            maxRight[j] = maxR

            maxL = max(maxL, height[i])
            maxR = max(maxR, height[j])

            i += 1
            j -= 1

        total = 0
        for i, h in enumerate(height):
            if min(maxLeft[i], maxRight[i]) - h > 0:
                total += min(maxLeft[i], maxRight[i]) - h

        return total

sol = Solution()
height = [0,2,0,3,1,0,1,3,2,1]
print(sol.trap(height))