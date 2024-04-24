from typing import List
from collections import defaultdict

# Time: O(N)
# Space: O(N)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)
        for y in range(9):
            for x in range(9):
                if board[y][x] == ".":
                    continue
                if board[y][x] in rows[y] or board[y][x] in columns[x] or board[y][x] in squares[(y//3, x//3)]:
                    return False
                rows[y].add(board[y][x])
                columns[x].add(board[y][x])
                squares[(y//3, x//3)].add(board[y][x])
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
