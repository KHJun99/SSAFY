import sys

sys.stdin = open('sample_input.txt')


def my_min(lst):
    min_val = float('inf')
    for i in lst:
        if min_val > i:
            min_val = i
    return min_val


def my_max(lst):
    max_val = float('-inf')
    for i in lst:
        if max_val < i:
            max_val = i
    return max_val


def my_sum(lst):
    total = 0
    for i in lst:
        total += i
    return total


T = int(input())
total = []
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(N - M + 1):
        lst_sum = my_sum(arr[i:i+M])
        total.append(lst_sum)

    result = my_max(total) - my_min(total)
    print(f'#{tc} {result}')
    total.clear()