import sys

sys.stdin = open('input.txt')


def my_max(lst):
    max_val = lst[0]
    for i in range(len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
    return max_val


def my_sum(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i]
    return total


def catch_fly(matrix, n, m):
    result = []  # 모든 경우의 합을 저장
    for row in range(n - m + 1):      # 파리채가 범위를 넘어가지 않도록 (정사각형 좌상단을 기준으로)
        for col in range(n - m + 1):
            # 파리채 범위 내의 모든 값을 저장할 리스트
            temp = []
            for i in range(m):        # M×M 범위
                for j in range(m):
                    temp.append(matrix[row + i][col + j])
            result.append(my_sum(temp))
    return my_max(result)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result = catch_fly(matrix, N, M)
    print(f'#{tc} {result}')
