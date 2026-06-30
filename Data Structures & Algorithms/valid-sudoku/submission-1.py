class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set)
        b = defaultdict(set)
        for i in range(9):
            row = set()
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    if num in row or num in col[j] or num in b[(i // 3, j // 3)]:
                        print((f'{num} is in row {i} or {num}' 
                        f'is in col {j} or {num} is in b ({(i // 3, j // 3)})'))
                        return False
                    row.add(num)
                    col[j].add(num)
                    b[(i // 3, j // 3)].add(num)

        return True
            