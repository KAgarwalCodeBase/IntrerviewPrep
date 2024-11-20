"""
88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/description/
Remark: Better approach for this to iterate from the end of given capacity of array's and then put element from nums1 end.
"""
from typing import List
class Solution:
    def merge(self, nums1: List[int], n: int, nums2: List[int], m: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        totalLength = n+m
        i = n-1
        j = totalLength -1
        while i>=0 and j>=m:
            nums1[j] = nums1[i]
            i-=1
            j-=1
        i = m
        j = 0
        k = 0
        while  i<totalLength and j<m:
            if nums1[i]<=nums2[j]:
                nums1[k] = nums1[i]
                i+=1
            else:
                nums1[k] = nums2[j]
                j+=1
            k+=1
        while i<totalLength:
            nums1[k] = nums1[i]
            i+=1    
            k+=1
        while j<m: 
            nums1[k] = nums2[j]
            j+=1
            k+=1
        