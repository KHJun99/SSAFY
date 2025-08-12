# [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리
import sys
from collections import deque

sys.stdin = open('sample_input.txt')

def bfs(start, goal):
    q = deque([start])              # 탐색을 시작할 큐에 시작 노드 추가
    visited[start] = True           # 시작 노드는 방문처리
    dist = [0] * (V + 1)            # dist[x] : 시작점에서 x까지의 거리(간선 수)

    # 큐에 아무것도 없을 때 까지 반복
    while q:
        cur = q.popleft()
        if cur == goal:
            return dist[cur]

        for nxt in node.get(cur, []):
            if not visited[nxt]:
                visited[nxt] = True
                dist[nxt] = dist[cur] + 1       # 거리 갱신
                q.append(nxt)

    return 0


# T : 테스트 케이스 개수
# V : 노드 개수, E : 간선 정보
# edge : 간선의 양쪽 노드 번호
# S, G : 축발 노드, 도착 노드
T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    visited = [False] * (V + 1)

    # 노드 연결 확인
    # ★ 무방향 인접 리스트
    node = {i: [] for i in range(1, V + 1)}
    for u, v in edge:
        node[u].append(v)
        node[v].append(u)  # 반대 방향도 추가

    print(f'#{tc} {bfs(S,G)}')

