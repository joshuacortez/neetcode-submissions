# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root: Optional[TreeNode], minval: int, maxval: int) -> bool:
            if not root:
                return True

            if not (minval < root.val < maxval):
                return False
            else:           
                check_left = valid(root.left, minval=minval, maxval=root.val)
                check_right = valid(root.right, minval=root.val, maxval=maxval)

                return check_left and check_right
            
        return valid(root, float("-inf"), float("inf"))
             