# Merge Sorted Array
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        cur1 = 0
        cur2 = 0
        prev = 0
        for i in range(n - 1):
            key = nums2[i]
            while nums1[prev] <= key and prev < m + i:
                prev += 1
            for j in range(m + i + 1, prev - 1, -1):
                nums1[j] = nums1[j - 1]
            nums1[prev] = key
        if n > 0:
            key = nums2[n - 1]
            while nums1[prev] <= key and prev < m + n - 1:
                prev += 1
            for j in range(m + n - 1, prev - 1, -1):
                nums1[j] = nums1[j - 1]
            nums1[prev] = key
