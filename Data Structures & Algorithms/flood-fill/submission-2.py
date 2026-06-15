from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # BFS outline
        # 1. setup
        # 2. boundary conditions
        # 3. add neighbors 

        nrows = len(image)
        ncols = len(image[0])

        # degenerate case
        if image[sr][sc] == color:
            return image

        start_color = image[sr][sc]
        queue = deque()
        queue.append((sr,sc))

        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                is_out_bounds = (r < 0) or (c < 0) or (r >= nrows) or (c >= ncols)
                if is_out_bounds:
                    continue
                is_diff_color = image[r][c] != start_color
                if is_diff_color:
                    continue
                
                image[r][c] = color
                queue.append((r+1,c))
                queue.append((r-1,c))
                queue.append((r,c+1))
                queue.append((r,c-1))
        
        return image




        