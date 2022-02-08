from typing import List

ROWS=9
COLS=9

SUB_ROWS=3
SUB_COLS=3

DIGITS=set([str(item) for item in range(1, 10)])

def display_matrix(board: List[List[str]]):
    print("<---")
    for row in range(ROWS):
        print(" ".join(board[row]))
    print("--->")

class Solution:
    def _construct_candidates_map(self, board: List[List[str]]):
        # Construct row candidates map
        self._row_candidates_map = {}
        for row in range(ROWS):
            self._row_candidates_map[row] = DIGITS - set(board[row])
            
        # Construct column candidates map
        self._col_candidates_map = {}
        for col in range(COLS):
            column = []
            for row in range(ROWS):
                column.append(board[row][col])
            self._col_candidates_map[col] = DIGITS - set(column)
            
        # Construct subbox candidates map
        self._subbox_candidates_map = {}
        for subrow in range(SUB_ROWS):
            for subcol in range(SUB_COLS):
                subbox = []
                for row in range(subrow*3, subrow*3+3):
                    for col in range(subcol*3, subcol*3+3):
                        subbox.append(board[row][col])
                self._subbox_candidates_map[(subrow, subcol)] = DIGITS - set(subbox)
        print("_subbox_candidates_map:", self._subbox_candidates_map)
        
    def _construct_candidates(self, board: List[List[str]], row: int, col: int) -> List[int]:
        self._construct_candidates_map(board)
        # Get row candidates
        row_candidates = self._row_candidates_map[row]
        # Get column candidates
        col_candidates = self._col_candidates_map[col]
        # Get subbox candidates
        subbox_candidates = self._subbox_candidates_map[(row//3, col//3)]
        return row_candidates & col_candidates & subbox_candidates
    
    def _is_solvable_sudoku(self, board: List[List[str]]) -> bool:
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] != ".":
                    continue
                # Construct candidates
                candidates = self._construct_candidates(board, row, col)
                if len(candidates) <= 0:
                    return False
                #print("row:", row, col, candidates)
                for candidate in candidates:
                    temp = board[row][col]
                    board[row][col] = str(candidate)
                    display_matrix(board)
                    #input()
                    if self._is_solvable_sudoku(board):
                        return True
                    board[row][col] = temp
                return False
                    
        return True
        
    def isSolvableSudoku(self, board: List[List[str]]) -> bool:
        self._construct_candidates_map(board)
        return self._is_solvable_sudoku(board)


if __name__ == "__main__":
    problem1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    #problem2 = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    #problem3 = [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
    solu = Solution()
    display_matrix(problem1)
    result = solu.isSolvableSudoku(problem1)
    print(result)
