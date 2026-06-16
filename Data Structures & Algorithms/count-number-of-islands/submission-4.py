from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # BFS that marks on enqueue
        # outline
        # 1. Setup
        # 2. Queue
        # 3. Boundary on neighbors
        # 4. Mark visited
        # 5. Add to queue
        
        nrows = len(grid)
        ncols = len(grid[0])
        visited_cells = set()
        n_islands = 0

        queue = deque() 

        for r in range(nrows):
            for c in range(ncols):
                is_land = grid[r][c] == "1"
                is_visited = (r,c) not in visited_cells 
                if is_land and is_visited:
                    # mark as visited all adjacent island cells
                    n_islands += 1

                    visited_cells.add((r,c))
                    queue.append((r,c))
                    while queue:
                        for i in range(len(queue)):
                            r, c = queue.popleft()
                            neighbors = [
                                [1,0],
                                [-1,0],
                                [0,1],
                                [0,-1],
                            ]
                            for (dr, dc) in neighbors:
                                new_r = r+dr
                                new_c = c+dc
                                is_out_bounds = (new_r < 0) or (new_c < 0) or (new_r >= nrows) or (new_c >= ncols)
                                is_visited = (new_r, new_c) in visited_cells

                                # skip non land
                                if is_out_bounds or is_visited:
                                    continue
                                    
                                is_land = grid[new_r][new_c] == "1"
                                if is_land:
                                    visited_cells.add((new_r,new_c))
                                    # check neighbors of this land
                                    queue.append((new_r,new_c))

        return n_islands




