class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = sorted((n, i) for i, n in enumerate(nums))
        l, r = 0, len(nums) - 1

        while l < r:
            cs = s[l][0] + s[r][0]
            if cs == target:
                return sorted([s[l][1], s[r][1]])
            if cs < target:
                l +=1
            else:
                r -=1
        return []

        