class Solution:
    def get_cell_index(self, i, j):
        return (i // 3) * 3 + j // 3
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_bits = [0] * 9
        col_bits = [0] * 9
        cell_bits = [0] * 9
    
        def is_bits_success(i, j, number):
            if row_bits[i] & (1 << number):
                return False
            if col_bits[j] & (1 << number):
                return False
            if cell_bits[self.get_cell_index(i, j)] & (1 << number):
                return False
            return True
        def add_number(i, j, number):
            bit = 1 << number
            row_bits[i] |= bit
            col_bits[j] |= bit
            cell_bits[self.get_cell_index(i, j)] |= bit

        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    number = int(board[i][j])
                    if not is_bits_success(i, j, number):
                        return False
                    add_number(i, j, number)
        return True