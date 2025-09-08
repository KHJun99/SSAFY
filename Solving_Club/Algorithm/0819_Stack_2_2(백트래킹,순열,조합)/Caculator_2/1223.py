# [S/W 문제해결 기본] 6일차 - 계산기 2
import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = input().strip()

    op = []
    stack = []
    for ch in arr:
        if ch.isdigit():
            stack.append(ch)
        elif ch == '*':
            op.append(ch)
        else:       # ch : '+'
            while op and op[-1] == '*':
                stack.append(op.pop())
            op.append(ch)
    while op:
        stack.append(op.pop())

    result = []
    for ch in stack:
        if ch.isdigit():
            result.append(int(ch))
        elif ch == '+':
            b = result.pop()
            a = result.pop()
            result.append(a + b)
        else:
            b = result.pop()
            a = result.pop()
            result.append(a * b)

    print(f'#{tc} {result[-1]}')
