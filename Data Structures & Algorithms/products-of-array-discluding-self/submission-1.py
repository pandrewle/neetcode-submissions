class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefix = [1] * l
        suffix = [1] * l
        ans = [1] * l
        for i in range(1,l):
            prefix[i] = prefix[i-1] * nums[i-1]
            print(f'prefix at {i} is {prefix[i]}')
        for i in range(l-2,-1,-1):
            suffix[i] = suffix[i+1] * nums[i+1]
            print(f'suffix at {i} is {suffix[i]}')
        for i in range(l):
            ans[i] = prefix[i] * suffix[i]
        return ans