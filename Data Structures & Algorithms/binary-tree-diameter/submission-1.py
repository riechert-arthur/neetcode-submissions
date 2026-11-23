# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Take the max from each sub-tree
        
        max_diameter = 0

        # Helper function
        # Find the max length in each sub-tree
        def diameterOfBinaryTree_r(root: Optional[TreeNode]) -> int:
            
            nonlocal max_diameter

            left_height = 0
            right_height = 0

            # No sub tree => no length
            if root.left:
                left_height = diameterOfBinaryTree_r(root.left) + 1
            
            if root.right:
                right_height = diameterOfBinaryTree_r(root.right) + 1

            
            print(f"({left_height}, {right_height})")
            diameter = left_height + right_height
            max_diameter = max(diameter, max_diameter)
            return max(left_height, right_height)

        diameterOfBinaryTree_r(root)
        return max_diameter