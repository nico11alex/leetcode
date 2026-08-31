class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        mitad = len(nums) // 2
        if len(nums) % 2 != 0:
            return nums[mitad]
        else:
            return (nums[mitad] + nums[mitad-1]) / 2
        