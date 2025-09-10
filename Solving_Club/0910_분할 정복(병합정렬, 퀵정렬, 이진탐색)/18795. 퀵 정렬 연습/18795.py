# 연습문제 1. 퀵 정렬 연습 (D2)
"""
문제
- 다음 데이터를 퀵 정렬하는 함수를 작성하고 테스트하시오.
"""
# import sys
# sys.stdin = open('input.txt', 'r')


def partition(left, right):
    pivot = arr[left]
    i = left + 1
    j = right

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]

    return j


def quick_sort(left, right):
    if left < right:
        pivot = partition(left, right)
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = len(arr)

    quick_sort(0, N - 1)
    print(f'#{tc}', *arr)
