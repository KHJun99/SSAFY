# 풍선팡 2
import sys
sys.stdin = open('input1.txt')


def delta(lst, n, m):
    delta_lst = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    best = 0
    for row in range(n):
        for col in range(m):
            total = lst[row][col]
            for di, dj in delta_lst:
                row_d, col_d = row + di, col + dj
                if row_d < 0 or row_d >= n or col_d < 0 or col_d >= m:
                    continue
                total += lst[row_d][col_d]
            if total > best:
                best = total
    return best


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = delta(arr, N, M)
    print(f'#{tc} {result}')