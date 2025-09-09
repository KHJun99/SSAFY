# def my_max(lst):
#     max_value = lst[0]
#     for i in range(len(lst)):
#         if lst[i] > max_value:
#             max_value = lst[i]
#     return max_value
#
# def counting_sort(lst, k):
#     count = [0] * (k + 1)
#     temp = [0] * len(lst)
#
#     for i in range(len(lst)):
#         count[lst[i]] += 1
#
#     for i in range(1, len(count)):
#         count[i] += count[i - 1]
#
#     for i in range(len(lst) - 1, -1, -1):
#         count[lst[i]] -= 1
#         temp[count[lst[i]]] = lst[i]
#
#     return temp


import sys

sys.stdin = open('sample_input.txt')

def between_max_min(lst):
    max_value = lst[0]
    min_value = lst[0]
    max_idx = 0
    min_idx = 0
    for i in range(len(lst) -1 , -1, -1):
        if lst[i] > max_value:
            max_value = lst[i]
            max_idx = i

    for i in range(len(lst)):
        if lst[i] < min_value:
            min_value = lst[i]
            min_idx = i

    between = abs(max_idx - min_idx)
    return between

# T : 테스트 케이스
# N : 양수의 개수
# arr : N개의 양수

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = between_max_min(arr)
    print(f'#{i} {result}')