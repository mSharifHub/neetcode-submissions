# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeLinkedList(self, sub_left,sub_right):
        # this is the dummy variable to link the nodes
        dummy = ListNode(0)
        head = dummy
        tail = dummy

        while sub_left and sub_right:
            if sub_left.val  < sub_right.val:
                tail.next = sub_left
                sub_left = sub_left.next

            else:
                tail.next = sub_right
                sub_right = sub_right.next

            # move tail to the next
            tail = tail.next

        if sub_left:
            tail.next = sub_left

        if sub_right:
            tail.next  = sub_right


        return head.next
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ## Base case check if the lists are empty
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1 ) < len(lists) else None
                merged_lists.append(self.mergeLinkedList(list1, list2))

            lists = merged_lists

        return lists[0]

    

  
        