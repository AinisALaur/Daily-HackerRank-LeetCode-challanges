class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []


        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = -nums[i]

            l = i + 1
            h = len(nums) - 1

            while l < h:
                sumOfelements = nums[l] + nums[h]
                if sumOfelements == target:
                    result.append([nums[i], nums[l], nums[h]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < h:
                        l += 1

                elif sumOfelements > target:
                    h -= 1
                
                else:
                    l += 1

        return result

        

sol = Solution()
nums=[-1,0,1,2,-1,-4]
print(sol.threeSum(nums))