# [파이썬 S/W 문제해결 기본] 8일차 - 이진 탐색
import sys
sys.stdin = open('sample_input.txt')


def find_node():
    pass


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    bt = [[] for _ in range(N + 1)]
