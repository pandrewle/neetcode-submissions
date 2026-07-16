class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # i = 0
        # while i < len(nums):
        #     numPos = nums[i] - 1 # 0-index
        #     if i != numPos and nums[i] == nums[numPos]:
        #         return nums[i]
        #     elif i == numPos:
        #         i += 1
        #     temp = nums[numPos]
        #     nums[numPos] = nums[i]
        #     nums[i] = temp
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
