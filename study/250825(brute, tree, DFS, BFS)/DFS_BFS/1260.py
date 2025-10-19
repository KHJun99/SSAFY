# 백준_1260_DFS와 BFS (s2)
"""
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성

조건
방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
더 이상 방문할 수 있는 점이 없는 경우 종료
정점 번호는 1번부터 N번까지
"""
# N : 정점의 개수, M : 간선의 개수, V : 탐색을 시작할 정점의 번호
from collections import deque


def dfs(graph, start, visited, out):
    visited[start] = True
    out.append(start)
    for nxt in graph[start]:
        if not visited[nxt]:
            dfs(graph, nxt, visited, out)


def bfs(graph, start, n):
    visited = [False] * (n + 1)
    q = deque([start])
    visited[start] = True
    order = []
    while q:
        v = q.popleft()
        order.append(v)
        for nxt in graph[v]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
    return order


N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# 방문 순서 규칙: 작은 번호부터
for i in range(1, N + 1):
    # 중복 간선 제거 + 정렬 (중복 없다고 확신하면 set() 없이 sorted만 해도 됨)
    graph[i] = sorted(set(graph[i]))

# DFS
visited = [False] * (N + 1)
dfs_order = []
dfs(graph, V, visited, dfs_order)

# BFS
bfs_order = bfs(graph, V, N)

print(*dfs_order)
print(*bfs_order)