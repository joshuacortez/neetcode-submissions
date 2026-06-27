class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Definition of a Tree
        # it has no cycles
        # it is fully connected

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

        all_visited = set()
        def dfs(curr_node, adj_list, visited, prev_node = None) -> bool:
            nonlocal all_visited
            """
            True if it found a cycle, else False
            """
            if curr_node in visited:
                return True
            
            visited.add(curr_node)
            all_visited.add(curr_node)

            neighbors = adj_list.get(curr_node, [])
            for neighbor in neighbors:
                if prev_node is not None:
                    if neighbor == prev_node:
                        continue
              
                found_loop = dfs(neighbor, adj_list, visited, prev_node=curr_node)
                if found_loop:
                    return True

            return False

        has_loop = dfs(0, adj_list, set())
        is_complete = len(all_visited) == n

        is_complete = len(all_visited) == n
        if is_complete and not has_loop:
            return True
        else:
            return False