class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        # Iterate through grid
        for i in range(len(board)):
            for j in range(len(board[i])):
                current_value = board[i][j]
                if current_value != '.':
                    if (current_value + ' found in row ' + str(i)) in seen or (current_value + ' found in column ' + str(j)) in seen or (current_value + ' found in subgrid ' + str(i//3) + '-' + str(j//3)) in seen:
                        return False
                    seen.add(current_value + ' found in row ' + str(i))
                    seen.add(current_value + ' found in column ' + str(j))
                    seen.add(current_value + ' found in subgrid ' + str(i//3) + '-' + str(j//3))
        return True