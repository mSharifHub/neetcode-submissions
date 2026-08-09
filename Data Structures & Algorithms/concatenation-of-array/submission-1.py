class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
       nested = [nums,nums]

       flat = [item for sublist in nested for item in sublist]

       return flat