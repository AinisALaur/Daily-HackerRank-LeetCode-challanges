class Solution:
    def maxArea(self, heights: list[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxWater = 0

        while i < j:
            area = (j - i) * min(heights[i], heights[j])
            maxWater = max(maxWater, area)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -=1
        
        return maxWater

sol = Solution()
heights = [1,7,2,5,4,7,3,6]
print(sol.maxArea(heights))