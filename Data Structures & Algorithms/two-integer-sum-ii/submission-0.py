class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) <= 1:
            return []

        left = 0
        right = len(numbers) -1

        while left < right:
            currentSum = numbers[left] + numbers[right]

            if currentSum > target:
                right -=1
            elif currentSum < target:
                left +=1
            else:
                left_idx = left + 1
                right_idx = right + 1

                return[left_idx, right_idx]

        return []
        