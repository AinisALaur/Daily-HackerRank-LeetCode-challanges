class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxA = -1
        stack = []

        for i in range(len(heights)):
            start = i
            while len(stack) > 0 and stack[-1][1] > heights[i]:
                area = (i - stack[-1][0]) * stack[-1][1]
                if area > maxA:
                    maxA = area
                
                index, val = stack.pop()
                start = index

            stack.append([start, heights[i]])


        size = len(heights)
        while len(stack) > 0:
            area = (size - stack[-1][0]) * stack[-1][1]
            if area > maxA:
                maxA = area
            stack.pop()

        return maxA
    
sol = Solution()
print(sol.largestRectangleArea([2,1,5,6,2,3]))

