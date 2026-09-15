class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        box=[set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                value=board[r][c]
                if value == ".":
                    continue
                if value in row[r]:
                    return False
                else:
                    row[r].add(value)
                if value in col[c]:
                    return False
                else:
                    col[c].add(value)
                num=(r//3)*3+(c//3)
                if value in box[num]:
                    return False
                else:
                    box[num].add(value)
        return True
