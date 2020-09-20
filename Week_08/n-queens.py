class Solution:
    def solveNQueens(self, n: int):
        board = []  # 棋盘
        output = []  # 调整为规定输出格式

        # 建立棋盘
        boa = ["_"] * n
        for _ in range(n):
            board.append(boa[:])

        # 检查格子
        def check(i, j):
            temp = 1  # 设为1是因为最少要从上一行开始检查
            while temp <= i:  # 因为是从上往下，逐行下子，所以只需要考虑这一行是否和上面的相互冲突就行。
                if board[i - temp][j] == "Q":  # 同列检查
                    return -1
                if (j - temp >= 0) and (board[i - temp][j - temp] == "Q"):  # 左上斜方向检查
                    return -1
                if (j + temp < n) and (board[i - temp][j + temp] == "Q"):  # 右上斜方向检查
                    return -1
                temp += 1  # 如果当前行比较深，就再检查上上一行是否冲突
            return 1

        # 下棋开始
        def play(rowi):
            if rowi == n:
                for p in range(n):
                    print(board[p])
                return

            for ci in range(n):
                if check(rowi, ci) == 1:  # 如果这个格子没问题
                    board[rowi][ci] = "Q"  # 在这个格子里下皇后
                    play(rowi + 1)  # 去下一行找合适的格子
                    board[rowi][ci] = "_"  # ！！！ 这里比较重要 ！！！ #
            return

        play(0)