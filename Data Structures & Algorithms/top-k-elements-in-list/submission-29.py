class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        h = []
        for x in c:
            heapq.heappush(h, (c[x],x))
            if len(h) > k:
                heapq.heappop(h)
        return [x for freq,x in h]
        