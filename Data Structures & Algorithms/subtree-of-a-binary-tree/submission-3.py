# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def is_same_tree_r(root_1: Optional[TreeNode], root_2: Optional[TreeNode]) -> bool:
        
            if not root_1 and not root_2:
                return True
            elif not root_1 or not root_2:
                return False

            if root_1.val == root_2.val:
                return is_same_tree_r(root_1.left, root_2.left) and is_same_tree_r(root_1.right, root_2.right)
            else:
                return False

        def isSubtree_r(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

            if not root:
                return False

            is_same_tree = is_same_tree_r(root, subRoot)
            
            if not is_same_tree:
                return isSubtree_r(root.left, subRoot) or isSubtree_r(root.right, subRoot)

            return is_same_tree

        return isSubtree_r(root, subRoot)
            