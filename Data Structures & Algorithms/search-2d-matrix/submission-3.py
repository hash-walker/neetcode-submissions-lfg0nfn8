class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix:
            return False

        r = len(matrix)
        c = len(matrix[0])

        s = 0
        e = (r * c) - 1


        
        while s <= e:

            m = s + (e-s) // 2

            row_idx = m // c
            col_idx = m % c

            if matrix[row_idx][col_idx] > target:
                e = m - 1
            elif matrix[row_idx][col_idx] < target:
                s = m + 1
            else:
                return True        
        
        return False