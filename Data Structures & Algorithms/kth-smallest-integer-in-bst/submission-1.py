class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0

        def inorder(root: Optional[TreeNode], k:int) -> Optional[int]:
            nonlocal counter

            if not root:
                return None

            left = inorder(root.left, k)
            if left is not None:
                return left
            
            counter += 1
            if counter == k:
                return root.val
            
            return inorder(root.right, k)

        return inorder(root,k)