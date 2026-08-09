class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        visited = {}

        
        for idx, value in enumerate(nums):
            remainer = target  - value

            if remainer in visited:
                return [visited[remainer],idx]

            visited[value] = idx
        
        return []
            