# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root:
            return False

        queue = [root]

        while queue:
            node = queue.pop(0)

            check_queue = [(node,subRoot)]
            is_match = True


            while check_queue:
                p, q = check_queue.pop(0)

                if not p and not q:
                    continue

                if not p or not q or p.val != q.val:
                    is_match= False
                    break

                check_queue.append((p.left,q.left))
                check_queue.append((p.right,q.right))

            if is_match:
                return True


            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return False
                



        