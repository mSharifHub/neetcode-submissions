# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(node):
            if node is None:
                return []

            left_tree = dfs(node.left)
            current_node = [node.val]
            right_tree = dfs(node.right)


            return left_tree + current_node + right_tree


        arr = dfs(root)

        k_val = k - 1

        return arr[k_val]
        