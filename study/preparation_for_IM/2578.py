# 빙고
matrix = [list(map(int, input().split())) for _ in range(5)]
num = [list(map(int, input().split())) for _ in range(5)]

cnt = 0
bingo = 0
is_bingo = [[0] * 5 for _ in range(5)]
while bingo != 3:
    if bingo == 3:
        break
    for r in range(5):
        for c in range(5):
            for i in range(5):
                for j in range(5):
                    if matrix[r][c] == num[i][j]:
                        cnt += 1
                        is_bingo[i][j] = 1

    for a in range(5):
        if is_bingo[a].count(1) == 5:
            bingo += 1

    for a in range(5):
        for b in range(5):
            col_list = []
            col_list.append(is_bingo[b][a])
            if col_list.count(1) == 5:
                bingo += 1
    for a in range(5):
        for b in range(5):
            if a == b:
                lst = []
                lst.append(is_bingo[a][b])
                if lst.count(1) == 5:
                    bingo += 1

    print(cnt)