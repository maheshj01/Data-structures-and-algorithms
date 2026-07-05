### Problem 3142. Check if Grid Satisfies Conditions (Easy)
### Tags: Array
class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        result = True
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if((r < len(grid) - 1) and (grid[r][c] != grid[r+1][c])):
                    return False
                if((c < len(grid[0]) - 1) and (grid[r][c] == grid[r][c+1])):
                    return False
        return result

if __name__ == "__main__":
    print(Solution().satisfiesConditions([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))

