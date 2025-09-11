# [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬 (D3)
"""
문제
- N개의 정수를 정렬해 리스트 A에 넣고, A[N//2]에 저장된 값을 출력하는 프로그램 작성
"""
import sys
sys.stdin = open('5205_input.txt', 'r')


# def hoare_partition(left, right):
#     pivot = arr[left]
#     i = left + 1
#     j = right
#
#     while i <= j:
#         while i <= j and arr[i] <= pivot:
#             i += 1
#         while i <= j and arr[j] >= pivot:
#             j -= 1
#
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[left], arr[j] = arr[j], arr[left]
#     return j        # 현재 피봇의 위치
#
#
# def quick_sort(left, right):
#     if left < right:
#         pivot = hoare_partition(left, right)
#         quick_sort(left, pivot - 1)
#         quick_sort(pivot + 1, right)

# python 리스트의 가변성을 활용한 quick sort
def quick_sort(num_list):
    # base case
    # 요소가 하나만 있는 경우에는 더 이상 재귀를 돌지 않도록 return
    if len(num_list) <= 1:
        return num_list

    pivot = num_list[0]     # 기준 점은 가장 왼쪽 값을 선정
    left = []
    right = []
    for idx in range(1, len(num_list)):
        if num_list[idx] < pivot:
            left.append(num_list[idx])
        else:
            right.append(num_list[idx])

    return [*quick_sort(left), pivot, *quick_sort(right)]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # quick_sort(0, N - 1)
    # print(f'#{tc} {arr[N//2]}')
    result = quick_sort(arr)
    print(f'#{tc} {result[N//2]}')
