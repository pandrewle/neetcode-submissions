class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            numPos = nums[i] - 1 # 0-index
            if i != numPos and nums[i] == nums[numPos]:
                return nums[i]
            elif i == numPos:
                i += 1
            temp = nums[numPos]
            nums[numPos] = nums[i]
            nums[i] = temp

        return nums[0]
