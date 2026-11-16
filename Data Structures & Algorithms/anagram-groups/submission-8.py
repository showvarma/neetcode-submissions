
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for words in strs:
            group["".join(sorted(words))].append(words)
        return list(group.values())

        