import sys

sys.stdin = open('sample_input (5).txt')


T = int(input())

for tc in range(1, T + 1):
    arr = [list(input())for _ in range(5)]

    # 각 행의 길이 중 최대값 구하기
    max_len = 0
    for row in arr:
        if len(row) > max_len:
            max_len = len(row)

    # 각 행을 최대 길이에 맞춰 패딩
    for row in range(len(arr)):
        while len(arr[row]) < max_len:
            arr[row].append('*')

    # 세로로 읽기
    col_lst = []
    for i in range(max_len):
        for j in range(5):
            if arr[j][i] != '*':
                col_lst.append(arr[j][i])

    print(f'#{tc} ', *col_lst, sep='')

