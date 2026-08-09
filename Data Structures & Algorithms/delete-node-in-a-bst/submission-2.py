# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def get_min_node(node):
            current = node
            while current.left:
                current = current.left
            return current

        if not root:
            return None

        # searching for the node
        if key < root.val:
            root.left = self.deleteNode(root.left,key)
        
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # case target node has one children
        else:
            if not root.left:
                return root.right

            elif not root.right:
                return root.left

            # case target node has 2 children
            successor = get_min_node(root.right)
            root.val = successor.val

            # delete the successor node
            root.right = self.deleteNode(root.right, successor.val)

        return root












        if not root:
            return root
        if key > root.val:
           root.right = self.deleteNode(root.right,key)
        elif key < root.val:
           root.left = self.deleteNode(root.left,key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            current = root.right

            while current.left:
                current = current.left
            
            root.val = current.val
            root.right = self.deleteNode(root.right,root.val)
        return root
            

        