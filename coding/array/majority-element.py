"""
169. Majority Element
https://leetcode.com/problems/majority-element/description/
"""
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = None;
        count = 0
        for x in nums:
            if count==0 or ele==x:
                ele = x
                count += 1
            else:
                count -= 1
        return ele
