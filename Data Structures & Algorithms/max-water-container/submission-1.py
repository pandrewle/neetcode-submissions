class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxWater = -1
        while l < r:
            length = r - l
            height = min(heights[l], heights[r])
            water = length * height
            if water > maxWater:
                maxWater = water

            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        
        return maxWater
