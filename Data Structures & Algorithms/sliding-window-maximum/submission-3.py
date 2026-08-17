import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
     res = []
     localMax = []
     i, j = 0, 0
     while j < len(nums):
          while j - i + 1 <= k:
               heapq.heappush(localMax, (-nums[j], j))
               j += 1
          while localMax[0][1] < i:
               heapq.heappop(localMax)
          res.append(-localMax[0][0])
          i += 1

     return res