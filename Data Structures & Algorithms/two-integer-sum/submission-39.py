class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in c and c[diff] != i:
                return [c[diff], i]
            c[n] = i
        return []