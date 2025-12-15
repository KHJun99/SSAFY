# SWEA_2115_벌꿀채취 (A형)
"""
## [문제 정리]

- N x N 개의 벌통이 정사각형 모양으로 배치되어 있다.
    - 각 칸의 숫자는 벌통에 있는 꿀의 양을 나타내며 꿀의 양은 서로 다를 수 있다.

- 벌꿀을 채취하는 방법
    - 두 명의 일꾼이 존재
    - 각각의 일꾼은 가로로 연속되도록 M개의 벌통 선택 -> 꿀 채취
        - 단, 두 명의 일꾼이 선택한 벌통은 서로 겹치면 안된다.
    - 꿀을 채취하여 용기에 담아야 한다.
        - 단, 서로 다른 벌통에서 채취한 꿀은 섞이면 안된다.
        - 꿀을 채취할 때 모든 꿀을 한번에 채취해야 한다.
    - 두 일꾼이 채취할 수 있는 최대 양은 C
    - 상품가치 : 각 용기에 있는 꿀의 양의 제곱
        ex) 꿀의 양 : 6, 1, 8 -> 수익 : 36, 1, 64
- 두 일꾼이 꿀을 채취하여 얻을 수 있는 수익의 합이 최대가 되는 프로그램 작성
"""
import sys
sys.stdin = open('sample_input.txt')

def profit(n):
    return n^2

T = int(input())
for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    honeycomb = [list(map(int, input().split())) for _ in range(N)]

    tmp = []
    for r in range(N):
        for c in range(0, N-(M - 1)):
            honey = honeycomb[r][c:c + M]
            if sum(honey) == C:
                tmp.append((r, c))

    coordinate = []
    for r, c in tmp:
        coordinate.append((r, c))
        for idx in range(1, M):
            coordinate.append((r, c + idx))

    start, end = [], []
    for idx in range(len(coordinate)):
        if idx % 2 == 0:
            start.append(coordinate[idx])
        else:
            end.append(coordinate[idx])

    c = len(coordinate) // 2
    for idx in range(c - 1):
        if end[idx] == start[idx + 1]:
            start.pop(idx + 1)
            end.pop(idx)

    print(tmp)
    print(coordinate)

    print(start)
    print(end)

    exit()
