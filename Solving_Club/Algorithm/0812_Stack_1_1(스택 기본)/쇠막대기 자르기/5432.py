# 5432 쇠막대기 자르기
import sys
from collections import deque

sys.stdin = open('sample_input (5).txt')


def cutCrowBar(brackets):
    my_stack = deque([])

    fragments = 0

    for bi in range(len(brackets)):
        # print(my_stack, brackets[bi])
        if brackets[bi] == '(':
            my_stack.append('(')
        else:
            if brackets[bi-1] == '(':
                # RAZOR
                my_stack.pop()
                fragments += len(my_stack)
            else:
                my_stack.pop()
                fragments += 1

    return fragments


T = int(input().strip())

for test_case in range(1, T + 1):
    brackets = input().strip()

    result = cutCrowBar(brackets)

    print(f"#{test_case} {result}")