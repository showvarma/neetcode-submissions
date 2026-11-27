class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for rows in range(9):
            seen = set()
            for i in range(9):
                if board[rows][i] == ".":
                    continue
                if board[rows][i] in seen:
                    return False
                seen.add(board[rows][i])\
        
        for cols in range(9):
            seen = set()
            for i in range(9):
                if board[i][cols] == ".":
                    continue
                if board[i][cols] in seen:
                    return False
                seen.add(board[i][cols])
        
        for squares in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    rows = (squares // 3)* 3 + i
                    cols = (squares % 3)* 3 + j

                    if board[rows][cols] == ".":
                        continue
                    if board[rows][cols] in seen:
                        return False
                    seen.add(board[rows][cols])
        return True
        
        