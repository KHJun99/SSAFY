# 백준_1325_효율적인_해킹
"""
## [문제 정리]

- 김지민 : 해커 -> 회사를 해킹하려고 한다.
- 회사
    - N개의 컴퓨터로 이루어져 있다.
    - 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있다.
    - A가 B를 신뢰하는 경우:
        - B를 해킹하면, A도 해킹 가능

- 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때,
  한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를
  출력하는 프로그램 작성
"""
from collections import defaultdict

N, M = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

