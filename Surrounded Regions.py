class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        boarders = [
            ij
            for k in range(max(m, n))
            for ij in ((0, k), (m-1, k), (k, 0), (k, n-1))
        ]

        while boarders:
            i, j = boarders.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                boarders += (i, j-1), (i, j+1), (i-1, j), (i+1, j)

        for row in board:
            for i, cell in enumerate(row):
                if cell == 'S':
                    row[i] = 'O'
                else:
                    row[i] = 'X'
