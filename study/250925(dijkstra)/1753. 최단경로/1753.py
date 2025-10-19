# 백준_1753_최단경로 (G4)
'''
## [문제]
- 방향 그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하시오.
- 단, 모든 간선의 가중치는 10 이하의 자연수이다.
'''
import heapq
import sys

input = sys.stdin.readline

# V : 정점의 개수, E : 간선의 개수
V, E = map(int, input().split())
# K : 시작 정점 번호
K = int(input())

# 인접 리스트 방식 그래프 초기화
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    # u: 출발 노드, v: 도착 노드, w: 가중치
    u, v, w = map(int, input().split())
    graph[u].append((v, w))  # u → v (비용 w)

# 거리 배열 초기화
INF = 10 ** 15
dist = [INF] * (V + 1)   # 정점 번호는 1 ~ V 사용
dist[K] = 0              # 시작 정점까지의 거리는 0

# 우선순위 큐(최소 힙)
pq = [(0, K)]  # (거리, 정점)

while pq:
    cur_dist, u = heapq.heappop(pq)

    # 이미 더 짧은 경로가 있다면 스킵
    if cur_dist > dist[u]:
        continue

    # u와 연결된 인접 노드 확인
    for v, w in graph[u]:
        # (현재 거리 + 간선 가중치) vs 기존 거리 비교
        if dist[v] > cur_dist + w:
            dist[v] = cur_dist + w
            heapq.heappush(pq, (dist[v], v))

# 결과 출력
for i in range(1, V + 1):
    # 도달 불가능한 정점은 "INF"로 표시
    print(dist[i] if dist[i] != INF else "INF")