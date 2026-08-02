from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        maxHeap = [-count for count in freq.values()]
        heapq.heapify(maxHeap)
        
        q = deque()
        time = 0
        while q or maxHeap:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                remainingCount = -heapq.heappop(maxHeap) - 1
                if remainingCount > 0:
                    q.append((-remainingCount, time+n))
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time