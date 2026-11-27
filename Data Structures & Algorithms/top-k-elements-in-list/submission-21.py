import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = {}
        for n in nums:
            c[n]=1+c.get(n,0)
        h = []
        for x in c:
            heapq.heappush(h, (c[x], x))
            if len(h) > k:
                heapq.heappop(h)   # kick out the least frequent

        return [x for freq, x in h]