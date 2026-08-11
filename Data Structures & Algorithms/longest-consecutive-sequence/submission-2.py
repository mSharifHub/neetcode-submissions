class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        longest = 0

        for number in nums:

            if (number - 1) not in num_set:

                length = 0
                while ( number + length) in num_set:
                    length +=1
                longest = max(longest, length)

        return longest
        