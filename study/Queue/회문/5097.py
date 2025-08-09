# [파이썬 S/W 문제해결 기본] 6일차 - 회전
import sys

sys.stdin = open('sample_input (4).txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(M):
        arr.append(arr.pop(0))
    print(f'#{tc} {arr[0]}')