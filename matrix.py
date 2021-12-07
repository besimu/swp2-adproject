import random

origin_board = [[0 for j in range(0, 9)] for i in range(0, 9)]
board = [[0 for j in range(0, 9)] for i in range(0, 9)]
row = [[0 for j in range(0, 10)] for i in range(0, 10)]
col = [[0 for j in range(0, 10)] for i in range(0, 10)]
diag = [[0 for j in range(0, 10)] for i in range(0, 10)]

terminate_flag = False


def board_init():
    seq_diag = [0, 4, 8]
    for offset in range(0, 9, 3):
        seq = [i for i in range(1, 10)]
        random.shuffle(seq)
        for idx in range(0, 9):
            i, j = idx // 3, idx % 3
            row[offset + i][seq[idx]] = 1
            col[offset + j][seq[idx]] = 1
            k = seq_diag[offset // 3]
            diag[k][seq[idx]] = 1
            origin_board[offset + i][offset + j] = seq[idx]


def make_sudoku(k):
    global terminate_flag
    global board

    if terminate_flag == True:
        return True

    if k > 80:
        for i in range(0, 9):
            for j in range(0, 9):
                board[i][j] = origin_board[i][j]
        terminate_flag = True
        return True

    i, j = k // 9, k % 9
    start_num = random.randint(1, 9)

    if origin_board[i][j] != 0:
        make_sudoku(k + 1)

    for m in range(1, 10):
        m = 1 + (m + start_num) % 9
        d = (i // 3) * 3 + (j // 3)
        if row[i][m] == 0 and col[j][m] == 0 and diag[d][m] == 0:
            row[i][m], col[j][m], diag[d][m] = 1, 1, 1
            origin_board[i][j] = m
            make_sudoku(k + 1)
            row[i][m], col[j][m], diag[d][m] = 0, 0, 0
            origin_board[i][j] = 0


def matrix():
    board_init()
    make_sudoku(0)
    k = []
    for i in range(0, 9):
        k.append(board[i])

    return k
