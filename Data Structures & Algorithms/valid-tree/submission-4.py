class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Definition of a Tree
        # it has no cycles
        # it is fully connected

        # shortcut
        # a valid tree with n nodes should have exactly n-1 edges
        # because every node except for the root should have an edge
        if len(edges) != n-1:
            return False

        # DFS outline
        # 1. setup
        # 2. base cases
        # 3. mark visited
        # 4. recursion
        # 5. backtracking

        adj_list = {}
        for edge in edges:
            source, target = edge
            if source not in adj_list:
                adj_list[source] = [target]
            else:
                adj_list[source].append(target)
            if target not in adj_list:
                adj_list[target] = [source]
            else:
                adj_list[target].append(source)

        visited = set()
        def dfs(curr_node, adj_list, prev_node = None) -> bool:
            """
            True if it found a cycle, else False
            """
            if curr_node in visited:
                return True
            
            visited.add(curr_node)

            neighbors = adj_list.get(curr_node, [])
            for neighbor in neighbors:
                if prev_node is not None:
                    if neighbor == prev_node:
                        continue
              
                found_loop = dfs(neighbor, adj_list, prev_node=curr_node)
                if found_loop:
                    return True

            return False

        has_loop = dfs(0, adj_list)
        is_complete = len(visited) == n

        is_complete = len(visited) == n
        if is_complete and not has_loop:
            return True
        else:
            return False