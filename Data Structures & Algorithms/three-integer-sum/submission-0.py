class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        i = 0
        while i < len(nums)-2:
            j = i + 1
            while j < len(nums)-1:
                k = j + 1
                while k < len(nums):
                    if nums[i] + nums[j] + nums[k] == 0:
                        ans.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                    k += 1
                j += 1
            i += 1
        return list(ans)
            

        