class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row = 0
        r_row = len(matrix)-1
        while l_row <= r_row:
            mid_row = ((r_row + l_row) // 2)
            l_col = 0
            r_col = len(matrix[0]) - 1
            mid_col = (r_col + l_col) // 2
            while l_col <= r_col:
                print(r_col)
                print(l_col)
                print(mid_row)
                print(mid_col)
                if matrix[mid_row][mid_col] == target:
                    return True
                elif matrix[mid_row][mid_col] <= target:
                    l_col = mid_col + 1
                else:
                    r_col = mid_col - 1
                mid_col = (r_col + l_col) // 2
            if r_col < 0 and r_col < l_col:
                r_row = mid_row - 1
            else:
                l_row = mid_row + 1

        return False