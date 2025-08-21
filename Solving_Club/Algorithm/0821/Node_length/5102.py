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
sys.stdin = open('5102_input.txt', 'r')



def bfs(S, G, V, adj_l):
    # 거리 배열: 방문 안 했으면 -1
    dist = [-1] * (V + 1)
    q = deque([S])
    dist[S] = 0

    while q:
        u = q.popleft()
        if u == G:                 # 목표를 꺼냈다면 그때의 거리가 최단거리
            return dist[u]
        for v in adj_l[u]:
            if dist[v] == -1:      # 아직 방문 안 했으면
                dist[v] = dist[u] + 1
                q.append(v)

    return 0 if dist[G] == -1 else dist[G]  # 도달 못하면 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split()) # 1번부터 V번 정점, E개의 간선
    adj_l = [[] for _ in range(V + 1)]  # 인접 리스트

    for _ in range(E):
        v1, v2 = list(map(int, input().split()))
        adj_l[v1].append(v2)
        adj_l[v2].append(v1)
    S, G = map(int, input().split())

    result = bfs(S, G, V, adj_l)
    print(f'#{tc} {result}')