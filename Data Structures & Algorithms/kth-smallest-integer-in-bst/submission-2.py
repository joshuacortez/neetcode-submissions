# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        root_res = root
        counter = k

        def inorder(root: Optional[TreeNode]) -> Optional[TreeNode]:
            nonlocal root_res, counter
            if not root:
                return None

            inorder(root.left)
            counter -= 1
            if counter == 0:
                root_res = root
            inorder(root.right)

        inorder(root)
        return root_res.val
