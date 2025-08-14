# Stack 2 - 연습문제 1 - 후위 유사 표기법 연습
import sys
sys.stdin = open('input.txt')

operator = {'+' : 1, '-' : 1, '*' : 2, '/' : 2}
T = int(input())
for tc in range(1, T + 1):
    arr = input().strip()
    stack = []
    result = []
    for i in arr:
        if i.isdigit():
            result.append(i)
        else:
            while stack and operator[stack[-1]] >= operator[i]:
                result.append(stack.pop())
            stack.append(i)
    while stack:
        result.append(stack.pop())
    result = ''.join(result)
    print(f'#{tc} {result}')