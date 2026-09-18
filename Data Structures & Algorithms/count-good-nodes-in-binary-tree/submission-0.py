# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def pre_order(node,max_value):

            if node is None:
                return 0

            res = 1 if node.val >= max_value else 0

            max_value = max(max_value,node.val)

            res += pre_order(node.left, max_value)
            res += pre_order(node.right,max_value)

            return res

        return  pre_order(root,float("-inf"))
            
        