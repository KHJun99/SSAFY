import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input().split()))

    max_value = ai[0]
    min_value = ai[0]
    for i in range(N):
        if ai[i] > max_value:
            max_value = ai[i]
        if ai[i] < min_value:
            min_value = ai[i]

    result = max_value - min_value
    print(f'#{case} {result}')
