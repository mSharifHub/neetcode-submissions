# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        stack = [(root, 1)]

        max_depth = 0

        while stack:

            current_node, current_depth = stack.pop()


            if current_node:
                max_depth = max(max_depth, current_depth)

                if current_node.left:
                    stack.append((current_node.left, current_depth + 1))

                if current_node.right:
                    stack.append((current_node.right, current_depth + 1))
        
        return max_depth

        

        