class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # DFS outline
        # 1. setup variables
        # 2. boundary conditions 
        # 3. recursive BFS to neighbors
        # 4. backtracking if needed

        nrows = len(image)
        ncols = len(image[0])
        visited = set()
        start_color = image[sr][sc]

        # do we want to modify the image in place or make a new copy?
        # if we modify it in place, we can only care about the colors we're changing
        # is there a risk of cascading recursive errors from modifying in place? 
            # perhaps not if we mark already as visited 

        def dfs(image, r, c, start_color):
            nonlocal visited

            nrows = len(image)
            ncols = len(image[0])
            # boundary conditions
            out_of_bounds = (r < 0) or (c < 0) or (r >= nrows) or (c >= ncols)
            if out_of_bounds:
                return
            is_diff_color = image[r][c] != start_color
            is_visited = (r,c) in visited
            if is_diff_color or is_visited:
                return 

            visited.add((r,c))
            dfs(image,r+1,c,start_color)
            dfs(image,r-1,c,start_color)
            dfs(image,r,c+1,start_color)
            dfs(image,r,c-1,start_color)
        
        dfs(image,sr,sc,start_color)
        for (r,c) in visited:
            image[r][c] = color
        return image

            