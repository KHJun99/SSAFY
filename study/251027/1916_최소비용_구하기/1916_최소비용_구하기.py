# 백준_1916_최소비용_구하기 (G5)
"""
## [문제 정리]
- N개의 도시 존재
    - 도시 번호는 1부터 N까지
- 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스 존재
- A번째 도시에서 B번째 도시까지 가는데 드는 최소 버스 비용을 구하시오.
"""
from heapq import heappop, heappush

def dijkstra(n, graph, start):

    # 최단거리 및 경로 추적용 배열 초기화
    dist = [INF] * (n + 1)
    prev = [-1] * (n + 1)

    # 시작 정점의 거리는 0
    dist[start] = 0

    # (거리, 정점) 형태의 튜플로 최소 힙 구성
    pq = [(0, start)]

    while pq:
        # 현재까지의 최소 거리 노드 꺼내기
        cur_dist, u = heappop(pq)

        # 이미 더 짧은 경로가 있으면 스킵 (중복 방지)
        if cur_dist > dist[u]:
            continue

        # u의 모든 이웃 노드 탐색
        for v, w in graph[u]:
            new_dist = cur_dist + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u
                # 힙에 새로운 거리 정보 추가
                heappush(pq, (new_dist, v))

    return dist, prev

# prev 배열을 이용해 최단 경로 복원
# def reconstruct_path(prev, start, target):
#     path = []
#     cur = target
#     while cur != -1:
#         path.append(cur)
#         if cur == start:
#             break
#         cur = prev[cur]
#     path.reverse()
#     return path

N = int(input())
M = int(input())
INF = float('inf')

edges = []
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    S, E, W = map(int, input().split())
    edges.append((S, E, W))

# u : 시작 정점, v : 도착 정점, w : 가중치
for u, v, w in edges:
    graph[u].append((v, w))
    # 만약 무향 그래프라면 아래 한 줄 추가
    # graph[v].append((u, w))

start, end = map(int, input().split())

dist, prev = dijkstra(N, graph, start)

# 만약 경로를 구해야 한다면 아래 코드 주석 제거
# path = reconstruct_path(prev, start, end)
# print(path)

print(dist[end])