"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # BFS outline
        # 1. setup
        # 2. boundary conditions
        # 3. DFS to neighbors
        # 4. backtracking if needed

        visited_nodes = {}

        def dfs(node):
            nonlocal visited_nodes

            if not node:
                return None

            if node.val in visited_nodes:
                return visited_nodes[node.val]
                
            cloned_node = Node(node.val,[])
            visited_nodes[node.val] = cloned_node
         
            for neighbor in node.neighbors:
                cloned_node.neighbors.append(dfs(neighbor))
                

            return cloned_node
    
        clone = dfs(node)
        
        return clone


