import random

class SudokuSolver:
    def __init__(self, board):
        self.board = board

    def is_valid(self, row, col, num):
        # Check the number is valid in the row or not
        for i in range(9):
            if self.board[row][i] == num:
                return False

        # Check the number is valid in the column or not
        for i in range(9):
            if self.board[i][col] == num:
                return False

        # Check if the number is valid in the 3x3 sub-grid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.board[i][j] == num:
                    return False

        return True

    def solve(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:  # Find an empty cell
                    numbers = list(range(1, 10))
                    random.shuffle(numbers)  # Shuffle numbers to ensure randomness
                    for num in numbers:  # Try shuffled numbers 1 to 9
                        if self.is_valid(row, col, num):
                            self.board[row][col] = num

                            if self.solve():
                                return True

                            self.board[row][col] = 0  # Backtrack

                    return False

        return True  # Puzzle solved

    def print_board(self):
        for row in self.board:
            print(" ".join(str(num) if num != 0 else '.' for num in row))

if __name__ == "__main__":
    # Example Sudoku puzzle (0 represents empty cells)
    board = [
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 0, 9, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 9]
    ]

    solver = SudokuSolver(board)
    print("Original Sudoku Puzzle:")
    solver.print_board()

    if solver.solve():
        print("\nSolved Sudoku Puzzle:")
        solver.print_board()
    else:
        print("\nNo solution exists for the given Sudoku puzzle.")
