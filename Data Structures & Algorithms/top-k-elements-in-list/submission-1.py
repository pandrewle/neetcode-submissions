class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket = [[] for i in range(len(nums)+1)]
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for n, c in count.items():
            bucket[c].append(n)
        ans = []
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                ans.append(n)
            if len(ans) == k:
                return ans