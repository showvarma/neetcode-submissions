class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p, z = 1, 0
        for n in nums:
            if n:
                p *= n
            else:
                z += 1
        if z > 1: return [0]*len(nums)

        res = [0]*len(nums)
        for i, n in enumerate(nums):
            if z: res[i] = 0 if n else p
            else:res[i] = p // n
        return res
