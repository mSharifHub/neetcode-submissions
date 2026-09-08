class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1

        while top <= bottom:
            middle_row = (top + bottom) // 2

            if target > matrix[middle_row][-1]:
                top = middle_row + 1

            elif target < matrix[middle_row][0]:
                bottom = middle_row - 1

            else:
                break

        if not (top <= bottom):
            return False
        
        current_row = (top + bottom) // 2
        left = 0
        right =  cols - 1

        while left <= right:
            middle = left + ((right - left ) // 2)

            if target > matrix[current_row][middle]:
                left = middle + 1
            elif target < matrix[current_row][middle]:
                right = middle - 1

            else:
                return True

        return False


                


