from typing import List

class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for r in range(n):
            for c in range(n):
                if (r == c or r + c == n - 1):  # Check diagonal elements
                    if grid[r][c] == 0:
                        return False
                else:  # Check non-diagonal elements
                    if grid[r][c] != 0:
                        return False
        return True