# 백준_13549_숨바꼭질 3 (G5)
'''
## [문제 요약]
- 상황: 수빈이가 점 N에 있고, 동생은 점 K에 있음 (범위: 0 ≤ N, K ≤ 100,000).
- 이동 규칙:
    1. 걷기: X → X-1 또는 X+1 (1초 소요)
    2. 순간이동: X → 2*X (0초 소요)
- 목표: 수빈이가 동생을 찾을 수 있는 가장 빠른 시간(최소 시간) 구하기.

## [문제 핵심]
- 일반적인 최단 경로 문제와 동일하나, 가중치가 0(순간이동) 또는 1(걷기) 두 가지.
'''
import sys
import heapq


def dijkstra(N, K):
    # N >= K 이면 무조건 뒤로 1칸씩 가야됨
    if N >= K:
        return N - K

    LIMIT = 100001
    INF = 10**15
    dist = [INF] * (LIMIT + 1)      # dist[x]의 의미 : x 까지의 거리 중 최적의 값
    dist[N] = 0

    pq = [(0, N)]

    while pq:
        # 현재까지 걸린 시간이 가장 적은 위치 꺼내기
        cur_t, x = heapq.heappop(pq)

        # 이미 더 짧은 경로가 있으면 무시
        if cur_t > dist[x]:
            continue

        # 목표 위치 K에 도착하면 정답 반환
        # 다익스트라의 원리 :
        #   - 어떤 노드가 힙에서 꺼내질 때, 그 순간 해당 노드까지의 최단 거리는 확정
        #   - dist[x]를 return 하는 것이 아닌 cur_t를 리턴하는 이유
        #   - dist[x]는 cur_t와 같은 값이거나 이미 갱신된 동일 값
        if x == K:
            return cur_t

        # 순간이동
        nx = x * 2
        if nx <= LIMIT and dist[nx] > cur_t:
            dist[nx] = cur_t
            heapq.heappush(pq, (cur_t, nx))

        # 걷기
        for nx in (x - 1, x + 1):
            if 0 <= nx <= LIMIT and dist[nx] > cur_t + 1:
                dist[nx] = cur_t + 1
                heapq.heappush(pq, (cur_t + 1, nx))
    return dist[K]


N, K = map(int, sys.stdin.readline().split())
result = dijkstra(N, K)
print(result)