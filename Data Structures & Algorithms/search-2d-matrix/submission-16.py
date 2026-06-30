class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row = 0
        r_row = len(matrix)-1
        l_col = 0
        r_col = len(matrix[0]) - 1
        while l_col <= r_col:
            mid_row = ((r_row + l_row) // 2)
            mid_col = (r_col + l_col) // 2
            while l_row <= r_row:
                print(l_row)
                print(r_row)
                print(mid_row)
                if ((matrix[mid_row][mid_col] == target) or
                (matrix[mid_row][l_col] == target) or
                (matrix[mid_row][r_col] == target)):
                    return True
                elif matrix[mid_row][l_col] < target:
                    l_row = mid_row + 1
                else:
                    r_row = mid_row - 1
                mid_row = ((r_row + l_row) // 2)
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                l_col = mid_col + 1
            else:
                r_col = mid_col - 1

        return False