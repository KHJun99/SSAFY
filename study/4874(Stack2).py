# [파이썬 S/W 문제해결 기본] 5일차 -Forth
T = int(input())
for tc in range(1, T + 1):
    stack = []
    tokens = input().split()    # 후기 표기식 입력
    result = 'error'    # 기본값 : 에러로 설정
    
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
            
        elif token in ['+', '-', '*', '/']:
            if len(stack) < 2:  # 스택에 피연산자가 2개 미만이면 잘못된 식
                break
            b = stack.pop()
            a = stack.pop()
            # 연산 수행
            if token == '+':
                stack.append(a + b)
            if token == '-':
                stack.append(a - b)
            if token == '*':
                stack.append(a * b)
            if token == '/':
                stack.append(a // b)    # 나눗셈의 경우 항상 나누어 떨어지기 때문
        elif token == '.':
            if len(stack) == 1:
                result = stack.pop()
            break
        else:
            break
                
    print(f'#{tc} {result}')
            