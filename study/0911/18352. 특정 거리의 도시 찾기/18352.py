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
from collections import deque


def bfs(start):
    # 각 도시까지의 최단 거리를 저장할 배열
    # -1로 초기화하여 아직 방문하지 않은 상태를 구분
    dist = [-1] * (N + 1)
    dist[start] = 0         # 시작 도시는 거리 0으로 설정
    q = deque([start])

    # 결과로 반환할 도시 목록
    result = []

    while q:
        cur = q.popleft()

        for nxt in graph[cur]:
            if dist[nxt] == -1:                 # 아직 방문하지 않은 도시라면
                dist[nxt] = dist[cur] + 1       # 최단 거리 갱신
                q.append(nxt)                   # 큐에 추가하여 계속 탐색

    # 최단 거리가 정확히 K인 도시들을 결과에 저장
    for i in range(1, N + 1):
        if dist[i] == K:
            result.append(i)

    return result


N, M, K, X = map(int, input().split())

# 그래프 초기화 (인접 리스트)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)

citys = bfs(X)

if citys:
    citys.sort()
    print(*citys, sep='\n')
else:
    print(-1)