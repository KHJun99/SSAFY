# [파이선 S/W 문제해결 기본] 4일차 - 괄호검사
import sys
sys.stdin = open('4866_input.txt')
parent = {
    ')': '(',
    '}': '{',
    ']': '[',
    '>': '<'
}

T = int(input())
for tc in range(1, T + 1):
    arr = list(input().strip())
    result = 0

    stack = []
    for ch in arr:
        if ch in '({[<':
            stack.append(ch)
        elif ch in ')}]>':
            if not stack and stack[-1] != parent.get(ch):
                result = 0
            stack.pop()
        else:
            continue
    if len(stack) != 0:
        result = 0
    else:
        result = 1
    print(f'#{tc} {result} ')