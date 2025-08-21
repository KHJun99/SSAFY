# [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리 (D2)
"""
문제
V개의 노드 개수와 방향성이 없는 E개의 간선 정보가 주어진다.
주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내는 프로그램을 만드시오.
예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경우, 두 개의 간선을 지나면 되므로 2를 출력한다.
노드 번호는 1번부터 존재하며, 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.
"""
from collections import deque
import sys
sys.stdin = open('5102_input.txt')


def bfs(S, G,  V):  # 시작정점 s, 마지막 정점 V
    visited = [0] * (V + 1)   # visited 생성
    q = deque()          # 큐 생성
    q.append(S)     # 시작점 인큐
    visited[S] = 1  # 시작점 방문표시
    while q:        # 큐에 정점이 남아있으면 front != rear
        t = q.popleft()    # 디큐
        for w in adj_l[t]:  # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
            if visited[w] == 0:
                q.append(w)     # w인큐, 인큐되었음을 표시
                visited[w] = visited[t] + 1
            if G in q:
                return 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split()) # 1번부터 V번 정점, E개의 간선
    adj_l = [[] for _ in range(V + 1)]  # 인접 리스트

    for _ in range(E):
        v1, v2 = list(map(int, input().split()))
        adj_l[v1].append(v2)
        adj_l[v2].append(v1)
    S, G = map(int, input().split())

    result = bfs(S, G, V)
    print(f'#{tc} {result}')