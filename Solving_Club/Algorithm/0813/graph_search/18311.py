# [Stack 1] 연습문제 3. 그래프 탐색
"""
조건
1. 시작 정점 : 1
2. 정점 탐색 시 숫자가 낮은 정점부터 방문
"""
import sys
sys.stdin = open('input (1).txt')

T = 1
V, E = map(int, input().split())        # V : 정점의 개수, E : 간선의 개수
vertex = list(map(int, input().split()))

# 도착 여부 확인용
visited = [False] * (V + 1)

# # 인접행렬
# adj = [[0] for _ in range(V + 1) for _ in range(V + 1)]
# for i in range(E):
#     s = vertex[i * 2]
#     e = vertex[i * 2 + 1]
#     adj[s][e] = 1
#     adj[e][s] = 1

# 인접 리스트
adj = [[] for _ in range(V + 1)]
for i in range(E):
    s = vertex[i * 2]
    e = vertex[i * 2 + 1]
    adj[s].append(e)
    adj[e].append(s)

for i in range(len(adj)):
    for j in range(len(adj[i]) - 1):
        if adj[i][j] < adj[i][j + 1]:
            adj[i][j], adj[i][j + 1] = adj[i][j + 1], adj[i][j]

order = []
start = 1
stack = [start]
visited[start] = True

while stack:
    cur = stack.pop()
    order.append(cur)

    # 큰 번호부터 push → pop 시 낮은 번호부터 방문됨
    # adj[cur]을 set으로 바꾸면 membership 검사 O(1)
    nbrs = set(adj[cur])
    for v in range(V, 0, -1):
        if v in nbrs and not visited[v]:
            visited[v] = True
            stack.append(v)
print(f'#{T}', '-'.join(map(str, order)))