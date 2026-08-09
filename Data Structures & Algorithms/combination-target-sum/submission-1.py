class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []

        def backtrack(start_index, current_comb, current_sum):

            if current_sum == target:
                result.append(current_comb.copy())
                return

            if current_sum > target:
                return

            
            for index in range(start_index, len(nums)):
                current_comb.append(nums[index])

                backtrack(index, current_comb, current_sum + nums[index])

                current_comb.pop()

        backtrack(0,[],0)
        return result



        