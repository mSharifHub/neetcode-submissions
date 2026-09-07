class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1]:
                left = 0
                right = len(row) - 1

                while left <= right:
                    middle = left + ((right - left) // 2)

                    if row[middle] == target:
                        return True
                    elif row[middle] < target:
                        left = middle + 1

                    else:
                        right = middle - 1

                return False
                
        return False
            



    




        