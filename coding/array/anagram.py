"""
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/description/
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        char = [0]*26
        for ind in range(len(s)):
            char1Ind = ord(s[ind])-97
            char2Ind = ord(t[ind])-97
            char[char1Ind]+=1
            char[char2Ind]-=1
        return sum(char)==0 and min(char)>=0