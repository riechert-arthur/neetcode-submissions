# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
                1
              /
             2
            /
           3   
"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        is_balanced = True

        # Perform a DFS
        def isBalanced_r(root: Optional[TreeNode]) -> int:

            nonlocal is_balanced
            
            # If there's no root,
            # There is no height.
            if not root:
                return -1

            # Assume left and right heights are 0
            # If there are none on this root
            left_height = 0
            right_height = 0

            if root.left:
                # Add 1 because there is an edge between the
                # child and the parent.
                left_height = isBalanced_r(root.left) + 1

            if root.right:
                right_height = isBalanced_r(root.right) + 1

            if abs(left_height - right_height) > 1:
                is_balanced = False
                
            return max(left_height, right_height)

        isBalanced_r(root)
        return is_balanced

        
