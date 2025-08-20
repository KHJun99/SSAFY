# [파이썬 S/W 문제해결 기본] 6일차 - 회전
import sys
sys.stdin = open('5097_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    rotate = M % N
    for i in range(rotate):
        arr.append(arr.pop(0))

    print(f'#{tc} {arr[0]}')