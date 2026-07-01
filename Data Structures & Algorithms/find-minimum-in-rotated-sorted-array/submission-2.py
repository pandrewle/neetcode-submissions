class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        minNum = nums[0]
        while l <= r:
            print(l)
            print(r)
            mid = (l+r) // 2
            print(mid)
            midNum = nums[mid]
            if midNum < minNum:
                minNum = midNum
                r = mid - 1
            else:
                l = mid + 1
        
        return minNum