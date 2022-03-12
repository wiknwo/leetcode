"""
    Time Complexity: O(n^2)
    Space Complexity: O(n^2 * m)
    
    where n is the size of the board and m is the size of the solution set
"""
class Solution:
    def totalNQueens(self, n):
        columns = set()
        positive_diagonals = set() # (r + c)
        negative_diagonals = set() # (r - c)
        solutions = [] # List to hold all possible N-Queen solutions
        chessboard = [(['.'] * n) for i in range(n)] # Creating n * n chesboard
        self.backtrack(0, n, chessboard, solutions, columns, positive_diagonals, negative_diagonals)
        return len(solutions)
    
    def backtrack(self, row, n, chessboard, solutions, columns, positive_diagonals, negative_diagonals):
        """Function to perform our backtracking in the N-Queens problem"""
        # Base case / stopping condition
        # We have found a valid N-Queens solution.
        # Row n means we have completed every single
        # row and we are out of bounds
        if row == n:
            # Add the current board to the solution set
            # but make a copy of the board because we will
            # use it in subsequent recursive calls.
            copy_of_chessboard = [''.join(r) for r in chessboard]
            solutions.append(copy_of_chessboard)
            return

        # We are going to try every column for the particular
        # row we are on to identify which position we can 
        # place the queen in.
        for column in range(n):
            # If eiter of these conditions are true then that means
            # we have to skip this position as the queen can be 
            # attacked if placed in this position
            if column in columns or (row + column) in positive_diagonals  or (row - column) in negative_diagonals:
                continue
            else:
                # Place queen in position
                columns.add(column)
                positive_diagonals.add(row + column)
                negative_diagonals.add(row - column)
                chessboard[row][column] = 'Q'

                # Inductive step: Do some work to shrink the problem space
                self.backtrack(row + 1, n, chessboard, solutions, columns, positive_diagonals, negative_diagonals)

                # Backtrack: Undo changes to check for more solutions
                columns.remove(column)
                positive_diagonals.remove(row + column)
                negative_diagonals.remove(row - column)
                chessboard[row][column] = '.'
        