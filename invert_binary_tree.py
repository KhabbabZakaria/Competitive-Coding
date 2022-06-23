#the very famous invert binary tree problem
#example: 
#   5              5
# 4   6 becomes  6   4


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        tempo = root.right
        root.right = root.left
        root.left = tempo
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        