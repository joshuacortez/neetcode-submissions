
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS outline
        # 1. setup queue and visited
        # 2. add first to queue
        # 3. pop from queue
        # 4. visit neighbors

        visited_land = set()

        n_rows = len(grid)
        n_cols = len(grid[0])

        n_islands = 0

        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == "0":
                    continue
                if (r,c) not in visited_land:
                    n_islands += 1
                    queue = deque()
                    queue.append((r,c))

                    while queue:
                        for i in range(len(queue)):
                            r,c = queue.popleft()

                            is_boundary = (r < 0) or (c < 0) or (r >= n_rows) or (c >= n_cols)
                            if is_boundary:
                                continue
                            
                            is_land = grid[r][c] == "1"
                            is_visited = (r,c) in visited_land
                            if is_land and not is_visited:
                                visited_land.add((r,c))
                                queue.append((r+1,c))
                                queue.append((r-1,c))
                                queue.append((r,c+1))
                                queue.append((r,c-1))
        
        return n_islands
