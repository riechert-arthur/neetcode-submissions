# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:  
        def invertTree_r(root: Optional) -> Optional[TreeNode]:
            if not root:
                return
            
            temp_right = root.right
            temp_left = root.left

            root.left = temp_right
            root.right = temp_left

            if root.left:
                self.invertTree(root.left)

            if root.right:
                self.invertTree(root.right)

        invertTree_r(root)
        return root