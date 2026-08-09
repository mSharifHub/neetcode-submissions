class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        results = [1] * len(nums)

        prefix = 1

        for idx in range(len(nums)):
            results[idx] = prefix
            prefix *= nums[idx]

        postfix = 1

        for idx in range(len(nums)-1, -1,-1):
            results[idx] *= postfix
            postfix *= nums[idx]

        return results

