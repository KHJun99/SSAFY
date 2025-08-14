# [파이썬 S/W 문제해결 기본] 5일차 - Forth
import sys
sys.stdin = open('4874_input.txt')

T = int(input())
for tc in range(1, T + 1):
    arr = input().split()   # 공백 기준 토큰 분리
    stack = []
    result = 'error'

    for token in arr:
        if token.isdigit():  # 숫자면 push
            stack.append(int(token))
        elif token in ['+', '-', '*', '/']:  # 연산자면 pop 2회 후 계산
            if len(stack) < 2:
                break
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)
        elif token == '.':   # 마침표(종료)
            if len(stack) == 1:  # 스택에 결과 1개면 OK
                result = stack.pop()
            break
        else:  # 잘못된 입력
            break

    print(f'#{tc} {result}')
