class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
            
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        
        # Step 1: Find all treasure chests (0) and add them to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    
        # Step 2: Multi-source BFS spreading out from all chests simultaneously
        while queue:
            r, c = queue.popleft()
            
            # Check all 4 directions (Up, Down, Left, Right)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                
                # If neighbor is within bounds AND is an unvisited land cell (INF)
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                    # The distance to this neighbor is the current cell's distance + 1
                    grid[nr][nc] = grid[r][c] + 1
                    # Put it in the queue to look at its own neighbors later
                    queue.append((nr, nc))