class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_arr = nums1 + nums2

        merged_arr.sort()

        n = len(merged_arr)

        if n%2 == 0:
            return (merged_arr[n//2] + merged_arr[(n//2)-1])/2
        else:
            return merged_arr[n//2]


