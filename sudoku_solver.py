class Solution:
    def isValid(self, board, row, column):
        for i in range(len(board)):
            if i != row and board[i][column] == board[row][column]:
                return False
        for j in range(len(board[0])):
            if j != column and board[row][j] == board[row][column]:
                return False
        i = 3 * (row // 3)
        while i < 3 * (row // 3 + 1):
            j = 3 * (column // 3)
            while j < 3 * (column // 3 + 1):
                if (i != row or j != column) and board[i][j] == board[row][column]:
                    return False
                j += 1
            i += 1
        return True
    
    def solver(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    for number in range(1, 10):
                        board[i][j] = str(number)
                        if self.isValid(board, i, j) and self.solver(board):
                            return True
                        board[i][j] = '.'
                    return False
        return True
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solver(board)