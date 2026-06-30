class Solution:
    import math

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        minSpeed = 0
        while l <= r:
            speed = (l+r) // 2
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / speed)
            print(l)
            print(r)
            print(speed)
            print(totalTime)
            if totalTime <= h:
                minSpeed = speed
                r = speed - 1
            else:
                l = speed + 1
            
        return minSpeed

