# [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로
def find_path(start, goal, adj):
    # 방문 여부를 체크하기 위한 배열 초기화 (노드 번호가 1부터 v까지 있으므로 v+1 크기로 생성)
    visited = [False] * (v + 1)
    # 시작 노드를 스택에 넣고 방문 처리
    stack = [start]
    visited[start] = True
    
    # 스택이 빌 때까지 반복 (더 이상 탐색할 노드가 없을 때까지)
    while stack:
        # 스택에서 노드를 하나 꺼냄
        current = stack.pop()
        # 현재 노드가 목표 노드라면 경로가 존재한다는 의미로 1 반환
        if current == goal:
            return 1
        
        # 현재 노드와 연결된 모든 노드 확인
        for next_node in adj[current]:
            # 방문하지 않은 노드라면
            if not visited[next_node]:
                # 스택에 추가하고 방문 처리
                stack.append(next_node)
                visited[next_node] = True
    
    # 모든 탐색이 끝났는데도 목표 노드에 도달하지 못했다면 경로가 없다는 의미로 0 반환
    return 0

T = int(input())  # 테스트 케이스 개수 입력

for test in range(1, T + 1):
    # v: 노드 개수, e: 간선 개수
    v, e = map(int, input().split())
    # 인접 리스트 초기화 (각 노드별 연결된 노드 정보를 저장할 빈 리스트 생성)
    adj = [[] for _ in range(v + 1)]
    
    # e개의 간선 정보 입력받기
    for _ in range(e):
        # start: 시작 노드, end: 도착 노드
        start, end = map(int, input().split())
        # 방향 그래프이므로 start에서 end로 가는 간선만 추가
        adj[start].append(end)
        
    # 경로 존재 여부를 확인할 시작 노드와 목표 노드 입력
    start_n, goal_n = map(int, input().split())
    # 경로 탐색 함수 호출하여 결과 저장
    result = find_path(start_n, goal_n, adj)
        
    # 테스트 케이스 번호와 결과 출력
    print(f'#{test} {result}')

# def root_graph(start, goal):
#     a = 0
#     if start in adj[start]:
#         while a != goal:
#             a = adj[start].pop()
#             return 1
#     return 0

# T = int(input())

# for test in range(1, T + 1):
#     v, e = map(int, input().split())
#     adj = [[i] for i in range(v + 1)]
    
#     for graph in range(1, e + 1):
#         start, goal = map(int, input().split())
#         adj[start].append(goal)
        
#         for link in range(1, e + 1):
#             if start in adj[link] and goal not in adj[link]:
#                 adj[link].append(goal)
                
#     start_n, goal_n = map(int, input().split())
#     result = root_graph(start_n, goal_n)
        
#     print(f'#{test} {result}')
 
