class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS outline
        # 1. Boundary conditions
        # 2. Mark visited
        # 3. BFS iterations
        # 4. backtracking (optional)

        visited_land = set()
        def dfs(grid, r, c) -> None:
            nonlocal visited_land

            nrows = len(grid)
            ncols = len(grid[0])

            # boundary conditions
            out_bounds_1 = (r < 0) or (c < 0)
            out_bounds_2 = (r >= nrows) or (c >= ncols)
            is_visited = (r,c) in visited_land
            
            boundary = out_bounds_1 or out_bounds_2 or is_visited
            if boundary:
                return None

            is_water = grid[r][c] == "0"
            if is_water:
                return None

            # mark visited
            visited_land.add((r,c))

            # BFS iterations
            dfs(grid, r+1, c)
            dfs(grid, r-1, c)
            dfs(grid, r, c+1)
            dfs(grid, r, c-1)

        n_islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited_land:
                    if grid[r][c] == "1":
                        n_islands +=1
                        dfs(grid,r,c)
              
        return n_islands

            