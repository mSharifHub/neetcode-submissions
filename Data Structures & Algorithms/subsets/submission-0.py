class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        subset = []

        def dfs(index):

            if index >= len(nums):
                result.append(subset.copy())
                return


            # Decision to include nums[i]
            subset.append(nums[index])
            dfs(index + 1)

            # Decision not to include nums[i]
            subset.pop()
            dfs( index + 1)

        dfs(0)
        return result

        