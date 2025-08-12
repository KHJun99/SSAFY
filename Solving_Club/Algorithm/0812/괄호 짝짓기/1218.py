# [S/W 문제해결 기본] 4일차 - 괄호 짝짓기
import sys
sys.stdin = open('input.txt')


# def my_push(item, size):
#     global top
#     top += 1
#     if top == size:
#         print('overflow!')
#     else:
#         stack[top] = item
#
#
# def my_pop():
#     global top
#     if top == -1:
#         print('underflow')
#         return 0
#     else:
#         top -= 1
#         return stack[top + 1]


def find_parentheses(lst):
    for ch in lst:
        if ch in '({[<':
            stack.append(ch)
        elif ch in ')}]>':
            # 스택이 비었거나, top과 짝이 아니면 실패
            if not stack or stack[-1] != parent[ch]:
                return 0
            stack.pop()
        # 그 외 문자는 무시(문제에 따라 없을 수도)

    # 모두 처리 후 스택이 비었으면 성공
    return 1 if not stack else 0


parent = {
    ')': '(',
    '}': '{',
    ']': '[',
    '>': '<'
}

for tc in range(1, 11):  # SWEA 1218은 항상 10개 테스트 케이스
    stack = []
    N = int(input())      # 길이(실제 검증엔 사용 안하지만 입력 형식상 받아둠)
    arr = list(input().strip())
    result = find_parentheses(arr)
    print(f'#{tc} {result}')
