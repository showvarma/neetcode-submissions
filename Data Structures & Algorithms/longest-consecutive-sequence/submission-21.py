class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        maxl = 0
        for n in num_set:
            if n - 1 not in num_set:
                l = 1
                while n + l in num_set:
                    l += 1
                maxl = max(maxl, l)
        return maxl