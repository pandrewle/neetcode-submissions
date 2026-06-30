class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            if (n-1) not in nums:
                curr = 1
                while n+curr in nums:
                    curr += 1
                if curr > ans:
                    ans = curr

        return ans