# [파이썬 S/W 문제해결 기본] 5일차 - Forth
import sys

sys.stdin = open('sample_input.txt')

def Forth(lst):
    stack = []
    result = 0
    op = ['+', '*', '%', '/', '//', '.']
    for i in lst:
        if i.isdigit():
            stack.append(int(i))
        else:
            print(i)

    return stack

T = int(input())

for i in range(1, T + 1):
    test_lst = list(map(str, input().split()))

    result = Forth(test_lst)

    print(f'#{i} {result}')


