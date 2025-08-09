import sys

sys.stdin = open('input.txt')


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

    sorted_lst = []
    for idx in range(N):
        min_val = my_min(arr)
        arr.remove(min_val)
        sorted_lst.append(min_val)
    print(f'#{tc}', *sorted_lst)
