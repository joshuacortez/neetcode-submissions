class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        unique_vals = set([f"{i}" for i in range(1,10)])

        row_hashmap = {row:set() for row in range(len(board))}
        col_hashmap = {col:set() for col in range(len(board[0]))}
        block_hashmap = {}
        for row in range(3):
            for col in range(3):
                block_hashmap[(row,col)] = set()

        for row in range(len(board)):
            for col in range(len(board[0])):
                char = board[row][col]
                if char == ".":
                    continue

                if char not in unique_vals:
                    return False
                
                if char in row_hashmap[row]:
                    return False
                else:
                    row_hashmap[row].add(char)

                if char in col_hashmap[col]:
                    return False
                else:
                    col_hashmap[col].add(char)

                block_id = (row//3, col//3)
                if char in block_hashmap[block_id]:
                    return False
                else:
                    block_hashmap[block_id].add(char)

        return True