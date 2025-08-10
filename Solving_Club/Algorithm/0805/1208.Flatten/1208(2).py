import sys

sys.stdin = open('input.txt')


def my_min(lst):
    min_val = float('inf')
    for i in lst:
        if min_val < i:
            min_val = i
    return min_val


for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N):
        left_1 = arr[i -1]
        left_2 = arr[i -2]
        right_1 = arr[i + 1]
        right_2 = arr[i + 2]
        side_lst = [left_1, left_2, right_1, right_2]
        min_val = my_min(side_lst)

