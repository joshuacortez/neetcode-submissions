# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ordered_nodes = []

        def inorder(root: Optional[TreeNode]) -> Optional[TreeNode]:
            nonlocal ordered_nodes

            if not root:
                return None
        
            inorder(root.left)
            ordered_nodes.append(root.val)
            inorder(root.right)
    
        inorder(root)
        return ordered_nodes[k-1]
            
            
