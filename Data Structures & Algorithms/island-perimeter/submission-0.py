class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        cols = len(grid[0])
        peri = 0
        
        for r in range(row):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Every land cell starts with 4 sides
                    peri += 4
                    
                    # If there's land directly above, they share a border (subtract 2)
                    if r > 0 and grid[r - 1][c] == 1:
                        peri -= 2
                        
                    # If there's land directly to the left, they share a border (subtract 2)
                    if c > 0 and grid[r][c - 1] == 1:
                        peri -= 2
                        
        return peri