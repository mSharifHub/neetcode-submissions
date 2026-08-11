class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
            
        nums.sort()

        left  = 0
        right  = left + 1

        max_sequence =  1
        current_sequence = 1

        while right < len(nums):

            diff = nums[right] - nums[left]

            if diff == 1:
                current_sequence +=1

            elif diff == 0:
                pass
            else:
                max_sequence = max(max_sequence, current_sequence)
                current_sequence = 1

            left +=1 
            right +=1

        max_sequence = max(max_sequence, current_sequence)

        return max_sequence
      
            


