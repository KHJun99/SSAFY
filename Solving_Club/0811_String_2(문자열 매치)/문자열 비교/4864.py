# 문자열 비교
# KMP 또는 보이어무어 사용
# import sys
# sys.stdin = open('4864_input.txt')
#
# T = int(input())
# for tc in range(1, T + 1):
#     pattern = list(input())
#     sen = list(input())
#     N = len(pattern)
#     M = len(sen)
#     i = 0
#     while i <= M - N:
#         j = N - 1
#         while j >= 0:
#             if pattern[j] != sen[i + j]:
#                 move = find(pattern, sen[i + M - 1])
#                 break
#             j = j - 1
#         if j == -1:
#             return True