"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # BFS outline
        # 1. setup
        # 2. add to queue
        # 3. add boundary conditions
        # 4. add neighbors

        if not node:
            return None

        queue = deque()
        queue.append(node)

        visited = {node:Node(node.val)} 

        while queue:
            for i in range(len(queue)):
                curr_node = queue.popleft()

                for neighbor_node in curr_node.neighbors:
                    if neighbor_node not in visited:
                        neighbor_clone = Node(neighbor_node.val)
                        visited[neighbor_node] = neighbor_clone
                        queue.append(neighbor_node)
                    else:
                        neighbor_clone = visited[neighbor_node]
                    visited[curr_node].neighbors.append(neighbor_clone)
                        
        return visited[node]
        