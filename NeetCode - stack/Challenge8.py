class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0] * len(temperatures)
        arr = []

        for dx, dy in enumerate(temperatures):
            while len(arr) > 0 and arr[-1][1] < dy:
                ans[arr[-1][0]] = dx - arr[-1][0]
                arr.pop()

            arr.append([dx, dy])

        return ans
            

sol = Solution()
print(sol.dailyTemperatures([30,38,30,36,35,40,28]))