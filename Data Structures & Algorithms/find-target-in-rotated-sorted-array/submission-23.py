class Solution:
    import math
    
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        deflection = (0, nums[l])
        while l <= r:
            mid = (l+r) // 2
            print(f'l: {l}')
            print(f'r: {r}')
            print("mid: " + str(mid))
            print("val: " + str(nums[mid]))
            if nums[mid] > deflection[1]:
                deflection = (mid, nums[mid])
                l = mid + 1
            else:
                r = mid - 1
        l = 0
        r = deflection[0]
        while l <= r:
            mid = (l+r) // 2
            print(f'left check {mid}')
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
                l = 0
        l = deflection[0]+1
        r = len(nums) - 1
        while l <= r:
            mid = math.ceil(l+r) // 2
            print(f'l: {l}')
            print(f'r: {r}')
            print(f'right check {mid}')
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1