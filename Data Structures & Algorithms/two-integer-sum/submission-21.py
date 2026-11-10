#Two Pointer Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = sorted(range(len(nums)), key=lambda i: nums[i])
        l, r = 0, len(nums) - 1
        while l < r:
            cur = nums[idx[l]] + nums[idx[r]]
            if cur == target:
                return sorted([idx[l], idx[r]])
            elif cur < target:
                l += 1
            else:
                r -= 1
        



        

        