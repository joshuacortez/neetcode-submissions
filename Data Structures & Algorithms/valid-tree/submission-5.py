from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # definition of a tree
        # 1. must have no cycles
        # 2. must be complete 

        # BFS outline
        # 1. setup
        # 2. queue
        # 3. base cases
        # 4. neighbor iteration
        # 5. neighbor base cases
        # 6. mark visited
        # 7. add to queue

        # quick shortcut, a tree with n nodes should have exactly n-1 edges
        if len(edges) != n - 1:
            return False

        # make the adjacency list
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

       
        visited = set([0])
        queue = deque([(0,None)])

        has_loop = False
        while queue:
            for i in range(len(queue)):
                curr_node, parent_node = queue.popleft()
                
                neighbors = adj_list.get(curr_node, [])
                for neighbor in neighbors:
                    if parent_node is not None:
                        if neighbor == parent_node:
                            continue

                    if neighbor in visited:
                        has_loop = True
                        break
                    visited.add(neighbor)
                    queue.append((neighbor,curr_node))
        
        is_complete = len(visited) == n
        is_valid = is_complete and not has_loop
        return is_valid
