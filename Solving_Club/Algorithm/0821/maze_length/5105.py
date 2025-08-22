# [파이선 S/W 문제해결 기본] 6일차 - 미로의 거리
"""
문제
NxN 크기의 미로에서 출발지 목적지가 주어진다.
이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.
경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.
"""
import sys
sys.stdin = open('5105_input.txt')
from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

