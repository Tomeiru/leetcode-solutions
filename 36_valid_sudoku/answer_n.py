from typing import List

# Time: O(N)
# Space: O(N)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        columns = []
        squares = []
        for _ in range(0, len(board)):
            rows.append([])
            columns.append([])
            squares.append([])
        for y in range(0, len(board)):
            for x in range(0, len(board[y])):
                if board[y][x] == ".":
                    continue
                rows[x].append(board[y][x])
                columns[y].append(board[y][x])
                squares[x // 3 + y // 3 * 3].append(board[y][x])
        for row in rows:
            if len(set(row)) != len(row):
                return False
        for column in columns:
            if len(set(column)) != len(column):
                return False
        for square in squares:
            if len(set(square)) != len(square):
                return False
        return True

if __name__ == '__main__':
    solution = Solution()
    print(f"Example 1: {solution.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])}")
    print(f"Example 2: {solution.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])}")
