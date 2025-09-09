# 백준_18352_특정 거리의 도시 찾기 (S2)
"""
문제
- 1부터 N번까지의 도시와 M개의 단방향 도로 존재
- 모든 도로의 거리는 1
- 특정한 도시 x로 부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인
  모든 도시들의 번호를 출력
- 출발 도시 x에서 도시 x로 가는 최단 거리는 항상 0

입력
- 첫 째줄 : N (도시의 개수), M (도로의 개수), K (거리 정보), X (출발 도시 번호)
- 둘 째줄 ~ M개 줄 : A, B 입력 (거리 정보) (A, B는 서로 다른 자연수)

출력
- 최단 거리가 K인 모든 도시의 번호를 한 줄에 오름차순으로 출력
- 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력
"""
import sys
sys.stdin = open('input.txt', 'r')


def bfs():


T = int(input())
for tc in range(T):
    N, M, K, X = map(int, input().split())

    graph = []
    for _ in range(M):
        s, e = map(int, input().split())
        graph.append((s, e))

