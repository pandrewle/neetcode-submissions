class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        i = 0
        while i < len(nums):
            curr = 1
            while nums[i]+curr in nums:
                curr += 1
            if curr > ans:
                ans = curr
            i += 1
        return ans