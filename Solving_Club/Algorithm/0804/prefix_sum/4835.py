import sys

def my_sum(lst):
    total = 0
    for i in range(len(lst)):
        total += int(lst[i])
    return total

sys.stdin = open('sample_input.txt')

T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))

    # 구간합 리스트 생성
    prefix_sum = []
    for i in range(N - M + 1):
        prefix_sum.append(my_sum(ai[i:i+M]))

    # 최대, 최소 찾기
    max_value = prefix_sum[0]
    min_value = prefix_sum[0]

    for val in prefix_sum:
        if val > max_value:
            max_value = val
        if val < min_value:
            min_value = val

    result = max_value - min_value
    print(f'#{case} {result}')
