class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # DFS outline
        # 1. setup
        # 2. boundary conditions
        # 3. mark visited
        # 4. recursion
        # 5. backtracking if needed

        nrows = len(heights)
        ncols = len(heights[0])
        
        reaches_atlantic = set()
        reaches_pacific = set()

        for r in range(nrows):
            for c in range(ncols):
                if (r == 0) or (c == 0):
                    reaches_pacific.add((r,c))
                if (r == nrows - 1) or (c == ncols - 1):
                    reaches_atlantic.add((r,c))
        
        def dfs(r, c, heights, visited) -> set:
            is_visited = (r,c) in visited
            if is_visited:
                return set()

            visited.add((r,c))

            nrows = len(heights)
            ncols = len(heights[0])
            neighbors = [
                [1,0],
                [-1,0],
                [0,1],
                [0,-1]
            ]
            for (dr, dc) in neighbors:
                new_r = r + dr
                new_c = c + dc

                is_out_bounds = (new_r < 0) or (new_c < 0) or (new_r >= nrows) or (new_c >= ncols)
                if is_out_bounds:
                    continue

                if heights[new_r][new_c] >= heights[r][c]:
                    visited.update(dfs(new_r, new_c, heights, visited))

            return visited

        new_reaches_atlantic = set()
        for (r,c) in reaches_atlantic:
            new_update = dfs(r, c, heights, set())
            new_reaches_atlantic.update(new_update)

        reaches_atlantic.update(new_reaches_atlantic)

        new_reaches_pacific = set()
        for (r,c) in reaches_pacific:
            new_update = dfs(r, c, heights, set())
            new_reaches_pacific.update(new_update)

        reaches_pacific.update(new_reaches_pacific)

        reaches_both = list(reaches_pacific & reaches_atlantic)
        return reaches_both
