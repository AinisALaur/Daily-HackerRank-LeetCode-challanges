class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        size = len(numbers)

        for i in range(size):
            diff = target - numbers[i]

            low = i + 1
            high = size - 1

            while low <= high:
                mid = int(low + (high - low) / 2)

                if numbers[mid] == diff:
                    return [i  + 1, mid + 1]

                if numbers[mid] < diff:
                    low = mid + 1
                
                elif numbers[mid] > diff:
                    high = mid - 1

sol = Solution()
print(sol.twoSum([2,3,4], 6))