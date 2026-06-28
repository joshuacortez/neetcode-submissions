from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # BFS outline
        # 1. setup
        # 2. queue
        # 3. base case
        # 4. neighbor iteration
        # 5. neighbor base case
        # 6. mark visited
        # 7. add to queue

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

        def bfs(start_node, adj_list, visited):
            queue = deque([start_node])
            visited.add(start_node)

            while queue:
                curr_node = queue.popleft()

                for neighbor in adj_list.get(curr_node, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            return visited

        components = []
        visited = set()
        for i in range(n):
            has_existing = False
            for component in components:
                if i in component:
                    has_existing = True
                    break

            if not has_existing:
                visited = bfs(i, adj_list, visited)
                components.append(visited)

        return len(components)