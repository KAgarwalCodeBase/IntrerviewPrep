"""
78: Subsets
https://leetcode.com/problems/subsets/description/
"""
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allSubsets = []
        def subset(ind, nums, ans):
            if ind>=len(nums):
                allSubsets.append(ans)
                return
            subset(ind+1,nums, ans+[nums[ind]])
            subset(ind+1,nums, ans)
        subset(0, nums, [])
        return allSubsets
            
