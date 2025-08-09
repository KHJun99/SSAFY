import sys

sys.stdin = open('sample_input (3).txt')

def find_min_sum():
    pass

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [[list(map(int, input().split()))] for _ in range(N)]

    result = find_min_sum(matrix)
    print(f'#{tc} {result}')