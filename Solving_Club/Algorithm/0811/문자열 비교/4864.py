# KMP 또는 보이어무어 사용

import sys
sys.stdin = open('4864_input.txt')

T = int(input())
for tc in range(1, T + 1):
    str1 = list(input())
    str2 = list(input())

    while True:
        if str1[-1] == 1: