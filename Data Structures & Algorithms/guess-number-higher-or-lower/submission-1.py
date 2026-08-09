# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        def helper(left,right):
            if left > right:
                return -1

            middle = (left + right) // 2
            result = guess(middle)

            if result > 0:
                return helper(middle + 1, right)

            elif result < 0:
                return helper(left, middle -1 )

            else:
                return middle

        return helper(1,n)



        
        