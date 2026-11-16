from collections import defaultdict
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l = defaultdict(list)
        for i in range(len(heights)):
            l[heights[i]] = names[i]
        d = dict(sorted(l.items(), key=lambda item: item[0], reverse=True))
        return list(d.values())
        
        