class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        i = 0
        while i < len(nums)-1:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] == -(nums[j] + nums[k]):
                    ans.add(tuple([nums[i], nums[j], nums[k]]))
                if nums[i] < -(nums[j] + nums[k]):
                    j += 1
                else:
                    k -= 1
            i += 1
            
        return list(ans)
            

        