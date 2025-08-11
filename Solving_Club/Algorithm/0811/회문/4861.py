import sys
sys.stdin = open('4861_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N , M = map(int, input().strip().split())
    arr = [list(map(str, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N - M + 1):
            word = arr[i][j : j + M]
            if word == word[::-1]:
                result = word
                break

    for j in range(N):
        for i in range(N - M + 1):
            word = [arr[i + k][j] for k in range(M)]
            if word == word[::-1]:
                result = word
                break

    print(f'#{tc} ', *result, sep = '')