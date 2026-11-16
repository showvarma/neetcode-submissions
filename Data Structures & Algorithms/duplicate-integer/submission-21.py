class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print(list(set(nums)))
        print(nums)
        return len(set(nums)) != len(nums)

        