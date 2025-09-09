import sys

sys.stdin = open('sample_input (4).txt')


def binary_search(target, page):
    start = 1
    end = page
    count = 0

    while start <= end:
        count += 1  # 탐색 시도 횟수 증가
        mid = (start + end) // 2

        if mid == target:
            return count

        elif mid > target:
            end = mid

        else:
            start = mid


T = int(input())
for tc in range(1, T + 1):
    P, A, B = map(int, input().split())

    result1 = binary_search(A, P)
    result2 = binary_search(B, P)

    print(f'#{tc}', end = ' ')
    if result1 < result2:
        print('A')
    elif result1 > result2:
        print('B')
    else:
        print(0)
