# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root:
            if key < root.val:
                root.left = self.deleteNode(root.left, key)
            elif key > root.val:
                root.right = self.deleteNode(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                child = root.right
                while child.left:
                    child = child.left
                root.val = child.val
                root.right = self.deleteNode(root.right, child.val)
            return root
        return
