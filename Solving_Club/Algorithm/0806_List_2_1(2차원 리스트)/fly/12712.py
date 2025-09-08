# 파리퇴치 3
import sys
sys.stdin = open('in1.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    p_delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x_delta = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

    max_val_1 = float('-inf')
    max_val_2 = float('-inf')
    for row in range(N):
        for col in range(N):
            total_1 = arr[row][col]
            total_2 = arr[row][col]
            for di, dj in p_delta:
                for cnt_1 in range(1, M):
                    row_p, col_p = row + di * cnt_1, col + dj * cnt_1
                    if 0 <= row_p < N and 0 <= col_p < N:
                        total_1 += arr[row_p][col_p]

            for dx, dy in x_delta:
                for cnt_2 in range(1, M):
                    row_x, col_y = row + dx * cnt_2, col + dy * cnt_2
                    if 0 <= row_x < N and 0 <= col_y < N:
                        total_2 += arr[row_x][col_y]

            if max_val_1 < total_1:
                max_val_1 = total_1
            if max_val_2 < total_2:
                max_val_2 = total_2
    if max_val_1 > max_val_2:
        result = max_val_1
    else:
        result = max_val_2

    print(f'#{tc} {result}')