import sys
from collections import deque

sys.stdin = open('sample_input.txt')


def melting_cheese():
    pass


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))

    fire_pit = deque()
