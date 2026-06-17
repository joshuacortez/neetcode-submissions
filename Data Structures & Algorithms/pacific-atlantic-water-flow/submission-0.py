from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # BFS outline
        # 1. setup
        # 2. queue
        # 3. iterate neighbors
        # 4. boundary conditions
        # 5. mark visited
        # 6. add to queue

        # idea: iterate through cell cell and
        # while iterating mark visited cells and also separately mark good cells
        # good cells are those that can reach both the atlantic and pacific

        # backtracking idea
        # 1. if the current cell's path are dead ends, then we can mark all cells a visited
        # 2. but if the current cell has a path, then we can only mark the starting cell as visited

        visited_cells = set()
        good_cells = set()

        def bfs(heights, r, c) -> bool:
            nonlocal visited_cells, good_cells

            visited_this_round = set()

            nrows = len(heights)
            ncols = len(heights[0])

            reaches_pacific = False
            reaches_atlantic = False

            visited_this_round.add((r,c))

            queue = deque()
            queue.append((r,c))
            while queue:
                for i in range(len(queue)):
                    curr_r, curr_c = queue.popleft()
                    neighbors = [
                        [1,0],
                        [-1,0],
                        [0,1],
                        [0,-1],
                    ]
                    for (d_r, d_c) in neighbors:
                        neighbor_r = curr_r + d_r
                        neighbor_c = curr_c + d_c

                        # found new good cell
                        if (neighbor_r < 0) or (neighbor_c< 0):
                            reaches_pacific = True
                        if (neighbor_r >= nrows) or (neighbor_c >= ncols):
                            reaches_atlantic = True
                        if reaches_pacific and reaches_atlantic:
                            print(f"Found good cell {(r,c)} with path {visited_this_round}")
                            good_cells.add((r,c))
                            visited_cells.add((r,c))
                            return True
                        
                        # decide which neighbors to add to the queue
                        in_ocean = (neighbor_r < 0) or (neighbor_c < 0) or (neighbor_r >= nrows) or (neighbor_c >= ncols)
                        if in_ocean:
                            continue 

                        lower_height = heights[neighbor_r][neighbor_c] <= heights[curr_r][curr_c]
                        visited_already = (neighbor_r, neighbor_c) in visited_this_round

                        # early termination
                        if lower_height and (neighbor_r, neighbor_c) in good_cells:
                            good_cells.add((r,c))
                            visited_cells.add((r,c))
                            return True
                            
                        if lower_height and not visited_already:
                            visited_this_round.add((neighbor_r,neighbor_c))
                            queue.append((neighbor_r,neighbor_c))

            # you've exhausted your queue means you're at a dead end
            visited_cells.update((visited_this_round))
            return False

        nrows = len(heights)
        ncols = len(heights[0])
        for r in range(nrows):
            for c in range(ncols):
                if (r,c) in visited_cells:
                    continue
                result = bfs(heights, r, c)
        
        return list(good_cells)

                        
                        



        
        