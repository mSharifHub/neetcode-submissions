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

            current = [(node,subRoot)]

            while current:
                p, q = current.pop(0)
                is_match = True

                if not p and not q:
                    continue

                if  not p or not q or p.val != q.val:
                    is_match = False
                    break

                current.append((p.left,q.left))
                current.append((p.right,q.right))

            if is_match:
                return True


            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    
        return False

                

                

                

        