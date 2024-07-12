# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        t = root.left
        root.left = root.right
        root.right = t

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


one = TreeNode(1)
three = TreeNode(3)
two = TreeNode(2, one, three)

six = TreeNode(6)
nine = TreeNode(9)
seven = TreeNode(7, six, nine)

root = TreeNode(4, two, seven)

tree = Solution().invertTree(root)

print(tree)
