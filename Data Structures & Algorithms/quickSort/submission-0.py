# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        self.helper(pairs,0,len(pairs) - 1)

        return pairs

    def helper(self,pairs:List['Pair'], start, end):
        if end - start + 1 <= 1:
            return

        pivot = pairs[end]
        left = start

        for i in range(start,end):
            if pairs[i].key < pivot.key:
                pairs[left], pairs[i] = pairs[i], pairs[left]
                left += 1

        pairs[left],pairs[end] = pairs[end], pairs[left]

        self.helper(pairs,start, left  - 1)
        self.helper(pairs,left + 1, end)
         