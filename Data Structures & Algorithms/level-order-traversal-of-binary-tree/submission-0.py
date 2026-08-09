# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        #Handling edge case when there is no nodes
        if not root:
            return []

        #Adding the first node and its links
        queue = deque([root])

        result = []

        #Iterating till we reach the end of the binary tree
        while queue:
            # getting current size of the current node level
            level_size = len(queue)
            # inner array to save the current level node values
            current_level_values = []
            # iterating on the level 
            for _ in range(level_size):
                # pop the node and add the current_level_values array
                current_node = queue.popleft()
                current_level_values.append(current_node.val)

                # adding left and right childrent to the queue
                if current_node.left:
                    queue.append(current_node.left)

                if current_node.right:
                    queue.append(current_node.right)

            result.append(current_level_values)

        return result