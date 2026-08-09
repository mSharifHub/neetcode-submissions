class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def helper(arr,left,right):

            if left > right:
                return -1


            middle = (left + right) // 2

            if target == arr[middle]:
                return middle

            elif target > arr[middle]:
               return  helper(arr,middle + 1, right)

            else:
                return helper(arr, 0, middle - 1)

        return helper(nums,0, len(nums) - 1)

        