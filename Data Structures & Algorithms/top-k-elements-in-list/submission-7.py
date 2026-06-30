class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        bucket = [[] for i in range(1+len(nums))]
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for c, v in count.items():
            print(f'Key {c}, value {v}')
            bucket[v].append(c)
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans

        return ans

