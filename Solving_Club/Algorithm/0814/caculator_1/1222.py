# [ S/W 문제해결 기본 ] 6일차 - 계산기1
import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):
    N = int(input())
    arr = input().strip()

    # 1) 중위표기 -> 후위표기 (연산자는 +만 존재)
    op_stack = []
    postfix = []
    for ch in arr:
        if ch.isdigit():
            postfix.append(ch)
        else:  # ch == '+'
            # 같은 우선순위(+)는 스택에 있는 것을 먼저 꺼냄(좌결합)
            while op_stack and op_stack[-1] == '+':
                postfix.append(op_stack.pop())
            op_stack.append(ch)
    while op_stack:
        postfix.append(op_stack.pop())

    # 2) 후위표기 계산
    stack = []
    for ch in postfix:
        if ch.isdigit():
            stack.append(int(ch))
        else:  # '+'
            a = stack.pop()
            b = stack.pop()
            stack.append(b + a)

    print(f'#{tc} {stack[-1]}')
