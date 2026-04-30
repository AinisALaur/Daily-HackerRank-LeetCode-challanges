class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        h = len(nums) - 1
        res = nums[0]

        while l <= h:
            if nums[l] < nums[h]:
                res = min(nums[l], res)
                break

            mid = l + (h - l) // 2
            res = min(nums[mid], res)
            
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                h = mid - 1
        
        return res

sol = Solution()
print(sol.findMin([3,4,5,6,1,2]))