# [모의 S/W 역량 테스트] 원자 소멸 시뮬레이션
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
dir = {'0': (-1, 0),
       '1': (1, 0),
       '2': (0, -1),
       '3': (0, 1)}
for tc in range(1, T + 1):
    N = int(input())
    atom = []
    for _ in range(N):
        x, y, heading, power = list(map(int, input().split()))
        atom.append((x, y, heading, power))

