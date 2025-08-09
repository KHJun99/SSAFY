import sys

sys.stdin = open('ex1_input.txt')


def my_sum(lst):
    total = 0
    for idx in lst:
        total += idx

    return total


def delta(lst, n):
    delta_lst = [[0, 1], [1, 0],
                 [0, -1], [-1, 0]]
    # 기준값 - 인접한 인덱스
    result = []

    for row in range(n):
        for col in range(n):
            # 차를 구하기 위한 기준 값
            center_value = lst[row][col]
            # 인접한 인덱스 값
            adj_value = []
            for di, dj in delta_lst:
                # 인덱스 설정
                n_row, n_col = row + di, col + dj
                # lst 범위를 넘어가지 않는 모든 경우의 수
                if 0 <= n_row < n and 0 <= n_col < n:
                    adj_value.append(lst[n_row][n_col])

            for idx in range(len(adj_value)):
                if center_value > adj_value[idx]:
                    result.append(center_value - adj_value[idx])
                else:
                    result.append(adj_value[idx] - center_value)
    return my_sum(result)


T = int(input())
for case in range(1, T + 1):
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))

    final_result = delta(matrix, N)

    print(f'#{case} {final_result}')