import sys

sys.stdin = open('sample_input (4).txt')


def my_sum(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i]
    return total


def find_subsets(s):
    n = len(s)
    subsets = []
    for i in range(1 << n):  # 2**n 만큼 반복 (모든 부분집합)
        subset = []
        for j in range(n):
            if (i >> j) & 1:  # j번째 비트가 1인지 확인
                subset.append(s[j])
        subsets.append(subset)
    return subsets


T = int(input())
my_set = [i for i in range(1, 13)]
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    count = 0

    subsets = find_subsets(my_set)
    for subset in subsets:
        if len(subset) == N and my_sum(subset) == M:
            count += 1
    print(f'#{tc} {count}')