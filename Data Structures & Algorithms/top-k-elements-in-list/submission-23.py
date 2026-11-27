from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        res = []
        l = []
        for x in c:
            res.append((c[x], x))
        res.sort()
        
        while k > 0:
            l.append(res.pop()[-1])
            k -= 1
        return l



        

        