import sys

sys.stdin = open('input.txt')


def my_max(lst):
    if not lst:
        return None
    max_value = lst[0]
    for idx in range(len(lst)):
        if lst[idx] > max_value:
            max_value = lst[idx]
    return max_value


def my_sum(lst):
    if not lst:
        return 0
    total = 0
    for idx in range(len(lst)):
        total += lst[idx]
    return total


def my_matrix_sum(lst):
    # 행 순환
    total = []
    for row in range(100):
        total.append(my_sum(lst[row]))

    # 열 순환
    for col in range(100):
        col_values = [lst[row][col] for row in range(100)]
        total.append(my_sum(col_values))

    # 대각선 합
    diag_values = [lst[i][i] for i in range(100)]
    total.append(my_sum(diag_values))

    # 역대각선 합
    diag_rev_values = [lst[99 - i][i] for i in range(100)]
    total.append(my_sum(diag_rev_values))
    return my_max(total)


for i in range(1, 11):
    T = int(input())
    matrix = []
    for j in range(100):
        arr = list(map(int, input().split()))
        matrix.append(arr)
    result = my_matrix_sum(matrix)
    print(f'#{T} {result}')

