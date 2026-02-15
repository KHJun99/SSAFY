# 백준_15591_MooTube (Silver) (G5)
"""
## [문제 정리]

- MooTube에서 농부 존의 소들은 재밌는 동영상들을 서로 공유 가능
- 소들은 MooTube에서 1~N까지 번호가 붙여진 N개의 동영상을 이미 올려놓았다.

- USADO : 두 동영상이 서로 얼마나 가까운 지를 측정하는 단위
- 존은 N-1개의 동영상 쌍을 골라서 직접 두 상의 USADO를 계산
- 존은 동영상들을 네트워크 구조로 바꿔서, 각 동영상을 정점으로 표현
- 존은 N-1개의 동영상 쌍을 골라서 어떤 동영상에서 다른 동영상으로 가는 경로가
  반드시 하나 존재하도록 결정
- 존은 임의의 두 쌍 사이의 동영상의 USADO를 그 경로의 모든 연결들의 USADO중 최소값으로 하기로 결정

- 존은 어던 주어진 동영상에 대해, 값 K를 정해서 
  그 동영상과 USADO가 K 이상인 모든 동영상이 추천되도록 할 예정
- 너무 많은 동영상이 추천되면 소들이 일하는 것이 방해될까봐 걱정
- 해결방안 : 적절한 K 값을 결정해야 한다.

- 어떤 K 값에 대한 추천 동영상의 개수를 묻는 질문 여러 개에 대답하시오.
"""
from collections import deque

# N: 동영상 개수, Q: 질문 개수
N, Q = map(int, input().split())

# 그래프 초기화 (인접 리스트)
graph = [[] for _ in range(N + 1)]

# N-1개의 간선 정보 입력
for _ in range(N-1):
    p, q, r = map(int, input().split())  # p-q 연결, 유사도 r
    graph[p].append((q, r))  # 양방향 그래프
    graph[q].append((p, r))


# Q개의 질문 처리
for _ in range(Q):
    k, v = map(int, input().split())  # k: 최소 유사도 기준, v: 시작 동영상

    # 방문 체크 배열
    visited = [False] * (N + 1)
    # BFS를 위한 큐
    queue = deque()
    # 추천 가능한 동영상 개수
    cnt = 0

    # 시작 노드 설정
    visited[v] = True
    # (현재 노드, 여기까지 오는 경로의 최솟값) - 시작은 무한대
    queue.append((v, float('inf')))

    # BFS 탐색 시작
    while queue:
        # 현재 노드와 여기까지의 USADO 값 꺼내기
        cur_node, min_usado = queue.popleft()

        # 현재 노드와 연결된 모든 노드 확인
        for next_node, edge_usado in graph[cur_node]:
            
            # 이미 방문한 노드는 건너뛰기
            if visited[next_node]:
                continue
            
            visited[next_node] = True  # 방문 처리

            # 다음 노드까지의 USADO 계산
            # = 지금까지의 최솟값과 현재 간선 유사도 중 최솟값
            new_usado = min(min_usado, edge_usado)

            # USADO가 k 이상이면 추천 가능
            if new_usado >= k:
                cnt += 1  # 추천 가능한 동영상 개수 증가
                queue.append((next_node, new_usado))  # 큐에 추가하여 계속 탐색
            # k 미만이면 더 이상 그 방향으로 탐색하지 않음

    print(cnt) 
