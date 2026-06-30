class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        i = 0
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:
                if a < -(nums[j] + nums[k]):
                    j += 1
                elif a > -(nums[j] + nums[k]):
                    k -= 1
                else:
                    ans.append([a, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
            
        return ans
            

        