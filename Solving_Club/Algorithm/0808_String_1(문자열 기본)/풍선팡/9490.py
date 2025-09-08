import sys
sys.stdin = open('input1.txt')


def my_max(lst1, lst2):
    if lst1 > lst2:
        return lst1
    else:
        return lst2


T = int(input())
for tc in range(1, T + 1):
    # 행, 열 입력
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # delta 구하기 (상, 하, 좌, 우)
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    max_sum = 0

    for row in range(N):
        for col in range(M):
            total = matrix[row][col]  # 여기서 초기화
            power = matrix[row][col]
            for di, dj in delta:
                for cnt in range(1, power + 1):
                    d_row, d_col = row + di * cnt, col + dj * cnt
                    if 0 <= d_row < N and 0 <= d_col < M:  # 범위 체크
                        total += matrix[d_row][d_col]
            max_sum = my_max(total, max_sum)

    print(f'#{tc} {max_sum}')
