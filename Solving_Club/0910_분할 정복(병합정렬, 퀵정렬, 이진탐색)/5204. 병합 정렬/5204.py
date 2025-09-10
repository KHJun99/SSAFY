# [파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬 (D3)
"""
문제
- N개의 정렬 대상을 가진 리스트 L을 분할할 때 L[0:N//2], L[N//2:N]으로 분할
- 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수 출력
- 정렬이 끝난 리스트 L에서 L[N//2] 원소 출력

입력
- 첫 번째 줄 : T (테스트 케이스 수)
- 두 번째 줄 : N (정수의 개수)
- 세 번째 줄 : ai (N개의 정수)
- 5 <= N <= 1,000,000
- 0 <= ai <= 1,000,000

출력
- N//2 번째 원소와 오른쪽 원소가 먼저 복사되는 경우의 수 출력
"""
import sys
sys.stdin = open('5204_input.txt', 'r')


def merge(left, right):
    # 병합 직전에 '왼쪽 마지막 > 오른쪽 마지막'이면 카운트
    global cnt
    if left and right and left[-1] > right[-1]:
        cnt += 1

    result = [0] * (len(left) + len(right))
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    while l < len(left):
        result[l + r] = left[l]
        l += 1

    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return result


def merge_sort(lst):
    if len(lst) == 1:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    left_lst = merge_sort(left)
    right_lst = merge_sort(right)

    merge_lst = merge(left_lst, right_lst)
    return merge_lst


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    sorted_lst = merge_sort(arr)
    print(f'#{tc} {sorted_lst[N//2]} {cnt}')