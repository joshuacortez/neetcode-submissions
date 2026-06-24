class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # first construct an adjacency matrix
        adj_list = {}
        for edge in prerequisites:
            target, source = edge
            if source not in adj_list:
                adj_list[source] = [target]
            else:
                adj_list[source].append(target)
            
        # DFS outline
        # 1. setup
        # 2. base cases
        # 3. mark visited
        # 4. recursion
        # 5. backtracking

        sure_no_loops = set()

        def dfs(curr_node, adj_list, visited) -> bool:
            nonlocal sure_no_loops
            """
            Returns True if a loop is found, else False
            """
            if curr_node in visited:
                return True

            visited.add(curr_node)

            neighbors = adj_list.get(curr_node, [])
            for neighbor in neighbors:
                has_loop = dfs(neighbor, adj_list, visited)
                if has_loop:
                    return True

            # if we did not find a loop, we backtrack
            sure_no_loops.add(curr_node)
            visited.remove(curr_node)
            return False

        for source in adj_list:
            if source not in sure_no_loops:
                has_loop = dfs(source, adj_list, set())
                if has_loop:
                    return False

        return True