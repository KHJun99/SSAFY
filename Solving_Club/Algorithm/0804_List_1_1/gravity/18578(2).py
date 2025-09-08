import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    box = list(map(int, input().split()))

    result = 0
    for i in range(N):
        gravity = 0
        for j in range(i + 1, N):
            if box[i] > box[j]:
                gravity += 1

        if result < gravity:
            result = gravity
    print(f'#{tc} {result}')