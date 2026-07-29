class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [[0] * 9 for _ in range(9)]
        cols = [[0] * 9 for _ in range(9)]
        boxes = [[0] * 9 for _ in range(9)]
        empty = []

        # Initialize
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    num = int(board[i][j]) - 1
                    rows[i][num] = 1
                    cols[j][num] = 1
                    boxes[(i // 3) * 3 + (j // 3)][num] = 1

        def x(idx):
            if idx == len(empty):
                return True

            i, j = empty[idx]
            box = (i // 3) * 3 + (j // 3)

            for k in range(9):
                if rows[i][k] == 0 and cols[j][k] == 0 and boxes[box][k] == 0:
                    board[i][j] = str(k + 1)

                    rows[i][k] = 1
                    cols[j][k] = 1
                    boxes[box][k] = 1

                    if x(idx + 1):
                        return True

                    board[i][j] = '.'
                    rows[i][k] = 0
                    cols[j][k] = 0
                    boxes[box][k] = 0

            return False

        x(0)