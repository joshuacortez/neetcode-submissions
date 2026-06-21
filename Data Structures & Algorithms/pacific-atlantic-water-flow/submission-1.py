from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # starting from the cells near one ocean
        # can I "flow up" to the other ocean?

        # BFS outline
        # 1. setup 
        # 2. queue
        # 3. find neighbors
        # 4. boundary conditions
        # 5. mark visited
        # 6. add to queue

        nrows = len(heights)
        ncols = len(heights[0])

        reaches_pacific = set()
        reaches_atlantic = set()

        for r in range(nrows):
            for c in range(ncols):
                if (r == 0) or (c == 0):
                    reaches_pacific.add((r,c))
                if (r == nrows - 1) or (c == ncols - 1):
                    reaches_atlantic.add((r,c))

        # perform BFS for each side
        def bfs(heights, shore_cells) -> set:
            # Return list of grid cells that can reach the shore cells

            visited = set()
            nrows = len(heights)
            ncols = len(heights[0])

            for (r,c) in shore_cells:
                queue = deque()
                visited.add((r,c))
                queue.append((r,c))

                while queue:
                    r,c = queue.popleft()
                    neighbors = [
                        [1,0],
                        [-1,0],
                        [0,1],
                        [0,-1],
                    ]
                    for (dr, dc) in neighbors:
                        new_r = r+dr
                        new_c = c+dc

                        is_visited = (new_r, new_c) in visited
                        is_out_bounds = (new_r < 0) or (new_c < 0) or (new_r >= nrows) or (new_c >= ncols)
                        if is_out_bounds or is_visited:
                            continue

                        is_higher = heights[new_r][new_c] >= heights[r][c]
                        if is_higher:
                            visited.add((new_r,new_c))
                            queue.append((new_r,new_c))

            return visited

        reaches_atlantic = bfs(heights, reaches_atlantic)
        reaches_pacific = bfs(heights, reaches_pacific)

        reaches_both = list(reaches_atlantic & reaches_pacific)
        return reaches_both
                        
                        
                        





        