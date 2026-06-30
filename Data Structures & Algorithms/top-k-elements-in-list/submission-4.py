class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        bucket = [[] for i in range(1+len(nums))]
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        for key in count:
            # print(f'Key {key}, value {count[key]}')
            bucket[count[key]].append(key)
        for i in range(len(bucket)-1, 0, -1):
            if len(ans) == k:
                return ans
            for num in bucket[i]:
                ans.append(num)

        return ans

