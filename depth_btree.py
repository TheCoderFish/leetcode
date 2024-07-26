# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


tn9 = TreeNode(9)
tn15 = TreeNode(15)
tn7 = TreeNode(7)
tn20 = TreeNode(20, tn15, tn7)
tn3 = TreeNode(3, tn9, tn20)


print(Solution().maxDepth(tn3))