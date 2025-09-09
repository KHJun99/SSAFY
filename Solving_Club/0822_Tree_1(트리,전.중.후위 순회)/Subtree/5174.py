# [파이썬 S/W 문제해결 기본] 8일차 - subtree
import sys
sys.stdin = open('5174_input.txt')

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    bt = [[] for _ in range(E + 2)]

    # 홀수, 짝수 번호로 구분
    for node, val in zip(arr[0::2], arr[1::2]):
        bt[node].append(val)

    cnt = 0
    stack = [N]
    while stack:
        cur = stack.pop(0)
        cnt += 1
        stack.extend(bt[cur])

    print(f'#{tc} {cnt}')