import sys

sys.stdin = open('input1.txt')


def delta(lst, n, m):
    delta_lst = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    max_val = lst[0][0]

    for row in range(n):
        for col in range(m):
            if lst[row][col] >= max_val:
                max_val = lst[row][col]
                start_x, start_y = row, col

                for di, dy in delta_lst:
                    if row < 0 or row >= n or col < 0 or col >= m:
                        row_d, col_d = start_x + di, start_y + di


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = delta(arr, N, M)

    print(f'#{tc} {result}')