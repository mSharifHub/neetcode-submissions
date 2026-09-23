class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        subset = []

        def dfs(idx):

            # Base Case
            if idx >= len(nums):
                result.append(subset.copy())
                return


            # include
            subset.append(nums[idx])
            dfs(idx + 1)

            # exclude
            subset.pop()
            dfs(idx + 1)


        dfs(0)


        return result

            
