import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [list(input().strip()) for _ in range(8)]
    size = 8
    count = 0
    # 가로 검사
    for i in range(size):
        for j in range(size - N + 1):
            word = arr[i][j : j + N]
            if word == word[::-1]:
                count += 1

    # 세로 검사
    for j in range(size):
        for i in range(size - N + 1):
            word = [arr[i + k][j] for k in range(N)]
            if word == word[::-1]:
                count += 1

    print(f'#{tc} {count}')