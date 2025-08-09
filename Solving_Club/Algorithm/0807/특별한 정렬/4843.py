import sys

sys.stdin = open('sample_input (4).txt')


def my_max(lst):
    max_val = lst[0]
    for i in range(len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
    return max_val


def my_min(lst):
    min_val = lst[0]
    for i in range(len(lst)):
        if lst[i] < min_val:
            min_val = lst[i]
    return min_val


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    special_lst = []
    for idx in range(N // 2):
        max_value = my_max(arr)
        arr.remove(max_value)
        special_lst.append(max_value)

        min_value = my_min(arr)
        arr.remove(min_value)
        special_lst.append(min_value)

    print(f'#{tc}', *special_lst[:10])

