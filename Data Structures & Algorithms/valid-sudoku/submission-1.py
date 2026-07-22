import math
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #loop through rows
        for row in range(9):
            #loop through each num in the row
            seen = set()
            for i in range(9):
                #check if num in row
                if board[row][i] == ".": #blank
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
                
        #loop through columns
        for col in range(9):
            #loop through each num in the column
            seen = set()
            for i in range(9):
                #check if num in row
                if board[i][col] == ".": #blank
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
                
            
            
        return True