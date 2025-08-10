import sys

sys.stdin = open('sample_input.txt')


def min_max(lst):
    min_val = float('inf')
    max_val = float('-inf')
    for i in lst:
        if min_val > i:
            min_val = i
        if max_val < i:
            max_val = i
    return max_val - min_val


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = min_max(arr)
    print(f'#{tc} {result}')