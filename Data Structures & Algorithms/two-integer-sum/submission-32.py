class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        i_nums = sorted((n, i) for i,n in enumerate(nums))

        while l < r:
            cs = i_nums[l][0] + i_nums[r][0]
            if cs == target:
                return sorted([i_nums[l][1], i_nums[r][1]])
            if cs < target:
                l += 1
            else:
                r -= 1
        return []
        