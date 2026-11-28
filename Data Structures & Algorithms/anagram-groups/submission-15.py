class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)


        for word in strs:
            s = [0]*26
            for x in word:
                s[ord(x) - ord('a')] += 1
            group[tuple(s)].append(word)
        return list(group.values())
            


        