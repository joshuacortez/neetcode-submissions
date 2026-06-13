# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()
        if not p and not q:
            return True
        elif (not p) or (not q):
            return False
        else:
            queue.append((p,q))

        while queue:
            for i in range(len(queue)):
                curr_p, curr_q = queue.popleft()

                if not curr_p and not curr_q:
                    pass
                elif (not curr_p) or (not curr_q):
                    return False
                else:
                    if curr_p.val != curr_q.val:
                        return False
                    
                    queue.append((curr_p.left, curr_q.left))
                    queue.append((curr_p.right, curr_q.right))

        return True