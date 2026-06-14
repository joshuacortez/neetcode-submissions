# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_d = 0
        def get_depth(root):
            nonlocal max_d
            if not root:
                return 0
            
            depth_left = get_depth(root.left)
            depth_right = get_depth(root.right)
            depth = 1 + max([depth_left, depth_right])
            diameter = depth_left + depth_right
            if diameter > max_d:
                max_d = diameter
            return depth

        get_depth(root)
        return max_d