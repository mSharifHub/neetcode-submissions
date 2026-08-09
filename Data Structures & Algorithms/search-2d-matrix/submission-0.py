class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows  = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1

        while top <= bottom:
            row = (top  + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row -1
            else:
                break

        if not (top <= bottom):
            return False

        left = 0
        right = cols -1
        row = (top + bottom) // 2

        while left <= right:
            middle= (left + right) // 2


            if target > matrix[row][middle]:
                left = middle + 1

            elif target < matrix[row][middle]:
                right = middle - 1

            else:
                return True

        return False



    




        