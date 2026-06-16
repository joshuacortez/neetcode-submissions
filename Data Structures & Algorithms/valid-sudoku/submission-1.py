class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        unique_set = set([f"{i}" for i in range(1,10)])
        def check_digits(digits: List[str]) -> bool:
            digits_only = [digit for digit in digits if digit != "."]
            digits_set = set(digits_only)

            # duplicate digits
            if len(digits_only) != len(digits_set):
                return False
            
            # illegal digits
            if digits_set - unique_set:
                return False

            return True

        nrows = len(board)
        ncols = len(board[0])
    
        for row in board:
            if not check_digits(row):
                print(f"Invalid row {row}")
                return False
        
        for col_idx in range(ncols):
            col = [row[col_idx] for row in board]
            if not check_digits(col):
                print(f"Invalid col {col}")
                return False
        
        for row_box_idx in range(3):
            for col_box_idx in range(3):
                box = []
                for row in range(3):
                    row_idx = row + 3*row_box_idx
                    for col in range(3):
                        col_idx = col + 3*col_box_idx
                        box.append(board[row_idx][col_idx])
                if not check_digits(box):
                    print(f"Invalid box {box}")
                    return False
                
        return True

        