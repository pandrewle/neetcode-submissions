class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_max, right_max = 0, 0
        totalArea = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] < left_max:
                    water = max(0, left_max - height[l])
                    totalArea += water
                else:
                    left_max = height[l]
                    
                l += 1
                
            else:
                if height[r] < right_max:
                    water = max(0, right_max - height[r])
                    totalArea += water
                else:
                    right_max = height[r]
                
                r -= 1

        return totalArea
            