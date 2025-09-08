# Stack 2 - 연습문제 1 - 후위 표기법 (Extra)
import sys
sys.stdin = open('sample_input.txt')

operator = {'+' : 1, '-' : 1, '*' : 2, '/' : 2}
T = int(input())
for tc in range(1, T + 1):
    arr = input().strip()
    stack = []
    result = []
    for i in arr:
        if i.isdigit():
            result.append(i)
        elif i == '(':               # 여는 괄호
            stack.append(i)
        elif i == ')':               # 닫는 괄호: '('까지 스택 팝
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            # 좌결합 연산자이므로, 스택 top의 우선순위가 >= 현재 연산자면 먼저 꺼냄
            while stack and stack[-1] != '(' and operator[stack[-1]] >= operator[i]:
                result.append(stack.pop())
            stack.append(i)

    while stack:
        result.append(stack.pop())
    result = ''.join(result)
    print(f'#{tc} {result}')