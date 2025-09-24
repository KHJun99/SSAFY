# 백준_13549_숨바꼭질 3
'''
## [문제 요약]
- 상황: 수빈이가 점 N에 있고, 동생은 점 K에 있음 (범위: 0 ≤ N, K ≤ 100,000).
- 이동 규칙:
    1. 걷기: X → X-1 또는 X+1 (1초 소요)
    2. 순간이동: X → 2*X (0초 소요)
- 목표: 수빈이가 동생을 찾을 수 있는 가장 빠른 시간(최소 시간) 구하기.

## [문제 핵심]
- 일반적인 최단 경로 문제와 동일하나,
    - 간선 가중치가 0(순간이동) 또는 1(걷기) 두 가지임.
    - 따라서 일반 BFS 대신 0-1 BFS(덱 사용) 혹은 우선순위 큐(Dijkstra) 활용이 적합.
'''
from collections import deque

def bfs(cur):
    q = deque([])
    q.append(cur)
    visited[cur] = 0
    if cur == K:
        return 0
    while q:
        n = q.popleft()
        if n == K:
            return visited[n]
        for nxt in (2*n, n-1, n+1):
            if 0 <= nxt < MAXRANGE and visited[nxt] == -1 and nxt == 2*n:
                q.append(nxt)
                visited[nxt] = visited[n]
            elif 0 <= nxt < MAXRANGE and visited[nxt] == -1 and nxt != 2*n:
                q.append(nxt)
                visited[nxt] = visited[n] + 1


MAXRANGE = 100001
N, K = map(int, input().split())
visited = [-1 for _ in range(MAXRANGE)]

print(bfs(N))