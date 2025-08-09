# [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사
def find_parentheses (str):
    stack = []
    pair = {')' : '(', '}' : '{'}
    
    for i in str:
        if i in '{(':
            stack.append(i)
        elif i in '})':
            # stack이 비어 있거나 짝이 안맞는 경우
            if not stack or stack[-1] != pair[i]:
                return 0
            stack.pop()
    return 1 if not stack else 0

T = int(input())

for i in range(1, T + 1):
    str = input()
    result = find_parentheses(str)
    print(f'#{i} {result}')