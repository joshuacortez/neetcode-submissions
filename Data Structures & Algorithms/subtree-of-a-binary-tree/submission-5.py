# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

    
        def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            elif (not p) or (not q):
                return False
            else:
                same_val = p.val == q.val
                same_left = is_same_tree(p.left, q.left)
                same_right = is_same_tree(p.right, q.right)
                return same_val and same_left and same_right

        if not root:
            return False   
        if is_same_tree(root, subRoot):
            return True
        else:    
            same_left = self.isSubtree(root.left, subRoot)
            same_right = self.isSubtree(root.right, subRoot)
            return same_left or same_right