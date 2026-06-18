class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0
        minutes_elapsed = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        if fresh_oranges == 0:
            return 0

        while queue and fresh_oranges > 0:
            minutes_elapsed += 1

            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    
                   
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2          
                        fresh_oranges -= 1        
                        queue.append((nr, nc))    
                        
        return minutes_elapsed if fresh_oranges == 0 else -1
