class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0
        
        def dfs(r, c):
            # Base case: boundary check and checking if it's water
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            
            # Mark the cell as visited by turning it into water
            grid[r][c] = '0'
            
            # Visit all 4 neighbors
            dfs(r + 1, c) # Down
            dfs(r - 1, c) # Up
            dfs(r, c + 1) # Right
            dfs(r, c - 1) # Left

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    # Found a new island!
                    island_count += 1
                    # Sink the entire island
                    dfs(r, c)
                    
        return island_count