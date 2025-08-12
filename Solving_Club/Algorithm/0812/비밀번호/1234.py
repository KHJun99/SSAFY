# [파이썬 S/W 문제해결 기본] 10일차 - 비밀번호
import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    length, arr = input().split()

    stack = []
    for i in range(length):
        if stack and stack[-1] == arr[i]:
            stack.pop()
        else:
            stack.append(arr[i])
    result = ''.join(stack)

    print(f'#{tc} {result}')