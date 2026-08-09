class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        def merge(left,middle,right):
            # left side of the array. middle + 1 because python slice is exclusive at end
            left_side = pairs[left: middle + 1]
            right_side = pairs[middle + 1: right + 1]

            # i to track the left side
            # j to track the right side
            # k to track the sorted array
            i, j = 0, 0
            k = left

            while i < len(left_side) and j < len(right_side):
                # to keep stability
                if left_side[i].key <= right_side[j].key:
                    pairs[k] = left_side[i]
                    i += 1
                else:
                    pairs[k] = right_side[j]
                    j +=1
                k +=1

            # to handle left overs from the iteration
            while i < len(left_side):
                pairs[k] = left_side[i]
                k +=1 
                i +=1

            while j < len(right_side):
                pairs[k] = right_side[j]
                k +=1
                j +=1


        def helper(left,right):

            if left >= right:
                return

            middle = (left + right) // 2

            helper(left, middle)
            helper(middle +1, right)

            merge(left,middle,right)

        helper(0, len(pairs) - 1)

        return pairs