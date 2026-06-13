# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        
        # if p and q are on diverging ends of root
        # then root is the lowest common ancestor

        # if either p or q is equal to root
        # then root is equal to lowest common anestor

        # otherwise, move to next node to decide

        is_left = (p.val < root.val) and (q.val < root.val)
        is_right = (p.val > root.val) and (q.val > root.val)
       
        if is_left:
            return self.lowestCommonAncestor(root.left, p, q)
        elif is_right:
            return self.lowestCommonAncestor(root.right, p, q)
        else:  
            # has an equal root, or diverging
            return root