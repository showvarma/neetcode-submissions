import heapq
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        n = len(nums)
        heap = heapq.heapify(nums)
        l = []
        while nums:
            l.append(heapq.heappop(nums))
        print(l)

        if n%2 == 0:
            median = (l[(n-1)//2] + l[n//2]) / 2
        else:
            median = l[n//2]
        return median





        