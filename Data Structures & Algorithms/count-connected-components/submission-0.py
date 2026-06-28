class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # DFS outline
        # 1. setup
        # 2. base case
        # 3. mark visited
        # 4. recursion
        # 5. backtracking (optional)

        adj_list = {}
        for edge in edges:
            node_a, node_b = edge
            if node_a not in adj_list:
                adj_list[node_a] = [node_b]
            else:
                adj_list[node_a].append(node_b)
            if node_b not in adj_list:
                adj_list[node_b] = [node_a]
            else:
                adj_list[node_b].append(node_a)

        def dfs(curr_node, adj_list, visited):
            if curr_node in visited:
                return

            visited.add(curr_node)

            for neighbor in adj_list.get(curr_node ,[]):
                dfs(neighbor, adj_list, visited)

            return visited

        components = []
        visited = set()
        for i in range(n):
            existing = False
            for component in components:
                if i in component:
                    existing = True
            
            if not existing:
                visited = dfs(i, adj_list, visited)
                components.append(visited)

        return len(components)