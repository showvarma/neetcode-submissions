class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)

        l = [x for x in nums if x <= target]
        m = [target]
        r = [x for x in nums if x > target]
        s = l + m + r
        return s.index(target)
        