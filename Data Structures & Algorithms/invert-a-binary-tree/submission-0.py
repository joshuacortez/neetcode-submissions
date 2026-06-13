# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        queue = deque()
        if root:
            queue.append(root)

        while queue:
            # pop out all the nodes from the previous level
            for i in range(len(queue)):
                curr = queue.popleft()

                curr.left, curr.right = curr.right, curr.left

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return root