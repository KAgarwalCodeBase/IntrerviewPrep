"""
48. Rotate Image
https://leetcode.com/problems/rotate-image/description/
"""
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose the matrix only for elements above major diagonal.
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(i,m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for j in range(m//2):
            for i in range(n):
                matrix[i][j], matrix[i][m-1-j] = matrix[i][m-1-j], matrix[i][j]
