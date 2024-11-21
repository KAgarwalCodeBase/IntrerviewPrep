"""
215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/description/

Using Counting sort
T.C: O(n+m)
S.C: O(m)
"""
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_val = min(nums)
        max_val = max(nums)
        count = [0]*(max_val - min_val + 1)
        for num in nums:
            count[num-min_val] += 1
        remain = k
        for num in range(len(count)-1, -1, -1):
            remain -= count[num]
            if remain <= 0:
                return num + min_val
        return -1